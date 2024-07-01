from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sq
from datetime import datetime
from tkcalendar import DateEntry
# Database connection
try:
    mydb = sq.connect(
        host='localhost',
        user='root',
        password='',
        database='cricket'
    )
    mycursor = mydb.cursor()
except sq.Error as e:
    print(f"Database connection error: {e}")
    messagebox.showerror("Error", "Failed to connect to the database. Check your connection settings.")

def fetch_match_schedule():
    query = """
    SELECT matches.date, t1.team_name, t2.team_name
    FROM matches
    JOIN teams t1 ON matches.team1_id = t1.team_id
    JOIN teams t2 ON matches.team2_id = t2.team_id
    ORDER BY matches.date
    """
    try:
        mycursor.execute(query)
        match_schedule = mycursor.fetchall()
        return match_schedule
    except sq.Error as e:
        print(f"Error fetching match schedule: {e}")
        messagebox.showerror("Error", f"Failed to fetch match schedule: {e}")
        return []

def schedule():
    global root
    root = Tk()
    root.title("Match Schedule")
    root.geometry('1200x750+0+0')
    root.resizable(0, 0)

    # Create a canvas and a vertical scrollbar
    canvas = Canvas(root)
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Title window
    titlewindow = Label(scrollable_frame, text='Match Schedule', font=('robotic', 20, 'bold'), bg='green', fg='white')
    titlewindow.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    addButton=Button(scrollable_frame,text='Add New Fixture', bg='blue', fg='white',font=('robotic', 13),command=fixture)
    addButton.place(x=20,y=12)
    datelb = Label(scrollable_frame, text='Date', font=('robotic', 15, 'bold'), bg='gray', fg='white')
    datelb.grid(row=1, column=0, sticky="nsew", padx=10, pady=10, ipadx=100, ipady=10)
    
    teamslb = Label(scrollable_frame, text='Teams', font=('robotic', 15, 'bold'), bg='#ffb703', fg='white')
    teamslb.grid(row=1, column=1, sticky="nsew", padx=10, pady=10, ipadx=300, ipady=10)

    # Fetch match schedule from database
    match_schedule = fetch_match_schedule()

    # Display match schedule
    for idx, match in enumerate(match_schedule):
        match_date = match[0].strftime('%d / %m / %Y')
        team1 = match[1]
        team2 = match[2]
        datelb = Label(scrollable_frame, text=match_date, font=('robotic', 16), bg='white', fg='black')
        datelb.grid(row=idx + 2, column=0, sticky="nsew", padx=10, pady=10, ipadx=100, ipady=10)
        
        teamslb = Label(scrollable_frame, text=f"{team1} vs {team2}", font=('robotic', 16), bg='white', fg='black')
        teamslb.grid(row=idx + 2, column=1, sticky="nsew", padx=10, pady=10, ipadx=300, ipady=10)
        
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    root.mainloop()
def fixture():
    Root=Toplevel(root)
    Root.title('Add new fixture')
    Root.geometry('800x300+0+0')
    Root.resizable(0,0)

    # Fetch team names from database
    query = "SELECT team_name FROM teams"
    mycursor.execute(query)
    teams = mycursor.fetchall()
    team_names = [team[0] for team in teams]

    # Create GUI elements
    newdate1=Label(Root,text='Date :',font=('robotic', 15))
    newdate1.place(x=20,y=20)
    newdate=DateEntry(Root,bd=1,relief='solid')
    newdate.place(x=120,y=20)
    newteam1lb=Label(Root,text='Team 1 :',font=('robotic', 15))
    newteam1lb.place(x=20,y=60)
    newteam1=ttk.Combobox(Root,font=('robotic',15))
    newteam1['values'] = team_names
    newteam1.place(x=120,y=60)
    newteam2lb=Label(Root,text='Team 2 :',font=('robotic', 15))
    newteam2lb.place(x=20,y=100)
    newteam2=ttk.Combobox(Root,font=('robotic',15))
    newteam2['values'] = team_names
    newteam2.place(x=120,y=100)

    # Function to add new fixture to database
    def add_fixture():
        date = newdate.get_date()
        team1 = newteam1.get()
        team2 = newteam2.get()

        if date and team1 and team2:
            query = """
            INSERT INTO matches (date, team1_id, team2_id)
            VALUES (%s, (SELECT team_id FROM teams WHERE team_name = %s), (SELECT team_id FROM teams WHERE team_name = %s))
            """
            try:
                mycursor.execute(query, (date, team1, team2))
                mydb.commit()
                messagebox.showinfo("Success", "New fixture added successfully")
                root.destroy()
                schedule()
            except sq.Error as e:
                messagebox.showerror("Error", f"Failed to add new fixture: {e}")

    # Submit button
    sumbitbtn=Button(Root,text='Sumbit',font=('robotic',15), command=add_fixture)
    sumbitbtn.place(x=350,y=150)
    
        
        


