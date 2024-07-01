from tkinter import *
from tkinter import messagebox, ttk
import pymysql as sq

# Establishing database connection
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

def fetch_team_name(team_id):
    try:
        mycursor.execute("SELECT team_name FROM teams WHERE team_id = %s", (team_id,))
        team_name = mycursor.fetchone()
        return team_name[0] if team_name else "Unknown"
    except sq.Error as e:
        print(f"Error fetching team name: {e}")
        messagebox.showerror("Error", f"Failed to fetch team name: {e}")
        return "Unknown"

def fetch_player_data(column_name):
    try:
        query = f"SELECT team_id, player_name, matches, runs, fours, sixes, wicket FROM players ORDER BY {column_name} DESC LIMIT 10"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    except sq.Error as e:
        print(f"Error fetching player data: {e}")
        messagebox.showerror("Error", f"Failed to fetch player data: {e}")
        return []

def display_data(data):
    # Clear previous data
    for widget in data_frame.winfo_children():
        widget.destroy()

    # Displaying data
    for row_index, row in enumerate(data):
        team_name = fetch_team_name(row[0])
        row = (team_name,) + row[1:]
        for col_index, item in enumerate(row):
            label = Label(data_frame, text=item, font=('Arial', 12), borderwidth=0, relief='solid')
            label.grid(row=row_index, column=col_index, sticky='nsew',ipadx=65,pady=5)

def search():
    search_value = searchCombo.get()
    column_map = {
        'Most Run': 'runs',
        'Most Wickets': 'wicket',
        'Most Sixes': 'sixes',
        'Most four': 'fours'
    }
    
    if search_value in column_map:
        column_name = column_map[search_value]
        data = fetch_player_data(column_name)
        display_data(data)
    else:
        messagebox.showwarning("Warning", "Please select a valid search option")

def State():
    global data_frame, searchCombo
    root = Tk()
    root.title("Player States")
    root.geometry("1200x600")

    # Title window
    titlewindow = Label(root, text='Player Performance & State', font=('robotic', 20, 'bold'), bg='green', fg='white')
    titlewindow.place(x=0, y=0, width=1200, height=50)

    # Search label and combobox
    searchlb = Label(root, text='Search By : ', font=('robotic', 20, 'bold'))
    searchlb.place(x=20, y=60)
    
    list = ['Select Option', 'Most Run', 'Most Wickets', 'Most Sixes', 'Most four']
    searchCombo = ttk.Combobox(root, font=('robotic', 15, 'bold'), values=list, state='readonly')
    searchCombo.current(1)
    searchCombo.place(x=200, y=60, width=300, height=40)
    
    searchbtn = Button(root, text='Search', font=('robotic', 15, 'bold'), bg='blue', fg='white', command=search)
    searchbtn.place(x=550, y=60, width=200)

    seprator = ttk.Separator(root, orient='horizontal')
    seprator.place(x=10, y=120, width=1200)

    # Header labels
    teamlb=Label(root,text='Team',font=('arial',15),bg='green',fg='white')
    teamlb.place(x=10, y=130, width=195,height=40)
    
    playearlb=Label(root,text='Player',font=('arial',15),bg='green',fg='white')
    playearlb.place(x=205, y=130, width=240,height=40)
    
    matchlb=Label(root,text='Match',font=('arial',15),bg='green',fg='white')
    matchlb.place(x=445,y=130, width=140,height=40)
    runlb=Label(root,text='Run',font=('arial',15),bg='green',fg='white')
    runlb.place(x=585,y=130, width=155,height=40)
    fourlb=Label(root,text="4's",font=('arial',15),bg='green',fg='white')
    fourlb.place(x=740,y=130, width=140,height=40)
    sixlb=Label(root,text="6's",font=('arial',15),bg='green',fg='white')
    sixlb.place(x=880,y=130, width=145,height=40)
    wicketlb=Label(root,text="Wicket",font=('arial',15),bg='green',fg='white')
    wicketlb.place(x=1025,y=130, width=145,height=40)
    

    # Frame for data display
    data_frame = Frame(root)
    data_frame.place(x=10, y=170, width=1180, height=420)

    root.mainloop()

State()
