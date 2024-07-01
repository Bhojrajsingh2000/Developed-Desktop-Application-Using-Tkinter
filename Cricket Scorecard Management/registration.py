from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sq
from datetime import datetime

try:
    mydb = sq.connect(
        host='localhost',
        user='root',
        password='',
        database='cricket'
    )
    mycouser = mydb.cursor()
except sq.MySQLError as e:
    messagebox.showerror("Database Connection Error", f"Error connecting to database: {e}")
    exit()

def refresh():
    try:
        countsql = 'select count(team_id) from teams'
        mycouser.execute(countsql)
        result = mycouser.fetchone()
        totalReg.config(text=f'Total Teams : {result[0]}')
        populate_treeview()
    except sq.MySQLError as e:
        messagebox.showerror("Database Error", f"Error fetching data: {e}")

def populate_treeview():
    try:
        # Clear existing data
        for row in treeview.get_children():
            treeview.delete(row)
        
        # Fetch data from database
        mycouser.execute('SELECT team_id, team_name FROM teams')
        for row in mycouser.fetchall():
            treeview.insert('', 'end', values=row)
    except sq.MySQLError as e:
        messagebox.showerror("Database Error", f"Error fetching data: {e}")

def RegistredTeam():
    global root,teamId, teamName, player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, treeview, totalReg
    root = Tk()
    root.title("Cricket Team Management")
    root.geometry("1350x750+0+0")
    root.resizable(False, False)

    # Title
    titlewindow = Label(root, text='Registration Teams And Players', font=('robotic', 20, 'bold'), bg='green', fg='white')
    titlewindow.place(x=10, y=0, width=1330, height=50)

    # First Frame
    firstframe = Frame(root, bd=0)
    firstframe.place(x=10, y=60, width=1330, height=100)

    # Team ID
    teamlb = Label(firstframe, text='Team ID :', font=('robotic', 15))
    teamlb.grid(row=0, column=0, padx=10, pady=10)
    teamId = Entry(firstframe, font=('robotic', 15), bd=1, relief='solid')
    teamId.grid(row=0, column=1, padx=10, pady=10)

    # Team Name
    teamNameLb = Label(firstframe, text='Team Name :', font=('robotic', 15))
    teamNameLb.grid(row=1, column=0, padx=10, pady=10)
    teamName = Entry(firstframe, font=('robotic', 15), bd=1, relief='solid')
    teamName.grid(row=1, column=1, padx=10, pady=10)

    # Date and Refresh Button
    date_today = datetime.today().strftime('%d / %m / %Y')
    datelb = Label(root, text=f'Date : {date_today}', font=('robotic', 12), bg='green', fg='white')
    datelb.place(x=20, y=10)
    refreshbtn = Button(root, text='Refresh', font=('robotic', 12), command=refresh)
    refreshbtn.place(x=1200, y=10)

    totalReg = Label(root, text="Total", font=('robotic', 15))
    totalReg.place(x=900, y=80)

    # Players Label
    playerlb = Label(root, text='Enter Players Name', font=('robotic', 17, 'bold'), width=1330, bg='orange', fg='white', anchor='w', padx=20)
    playerlb.place(x=10, y=160, width=1330, height=50)

    # Second Frame for Players
    secondFrame = Frame(root, bd=0)
    secondFrame.place(x=10, y=220, width=1330, height=300)

    # Players Entry Fields
    player_labels = []
    player_entries = []
    for i in range(11):
        row = i % 5
        col = (i // 5) * 2
        label = Label(secondFrame, text=f'Player {i + 1}', font=('robotic', 15))
        label.grid(row=row, column=col, padx=10, pady=10)
        entry = Entry(secondFrame, font=('robotic', 15), bd=1, relief='solid')
        entry.grid(row=row, column=col + 1, padx=10, pady=10)
        player_labels.append(label)
        player_entries.append(entry)

    player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11 = player_entries

    # Submit Button
    sumbitbtn = Button(secondFrame, text="Register Team", font=('robotic', 15), bg='green', fg='white', bd=1, relief='solid', command=Registration)
    sumbitbtn.place(x=465, y=260, width=400, height=40)

    # Treeview Frame
    treeview_frame = Frame(root)
    treeview_frame.place(x=10, y=530, width=1330, height=200)

    # Define treeview
    treeview = ttk.Treeview(treeview_frame, columns=('team_id', 'team_name'), show='headings')
    treeview.heading('team_id', text='Team ID')
    treeview.heading('team_name', text='Team Name')
    treeview.column('team_id', width=150)
    treeview.column('team_name', width=200)
    
    # Add scrollbar
    scrollbar = Scrollbar(treeview_frame, orient=VERTICAL, command=treeview.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    treeview.config(yscrollcommand=scrollbar.set)
    
    treeview.pack(fill=BOTH, expand=True)

    # Populate treeview with data
    populate_treeview()

    # Refresh the total number of teams
    refresh()

    root.mainloop()

def Registration():
    try:
        TeamId = int(teamId.get())
        TeamName = teamName.get().strip()

        if not TeamName:
            messagebox.showerror("Input Error", "Team name cannot be empty.")
            return

        PlayerNames = [player1.get().strip(), player2.get().strip(), player3.get().strip(), player4.get().strip(),
                       player5.get().strip(), player6.get().strip(), player7.get().strip(), player8.get().strip(),
                       player9.get().strip(), player10.get().strip(), player11.get().strip()]

        if any(not player for player in PlayerNames):
            messagebox.showerror("Input Error", "All player names must be filled.")
            return

        sql = 'INSERT INTO teams (team_id, team_name) VALUES (%s, %s)'
        mycouser.execute(sql, (TeamId, TeamName))
        mydb.commit()

        for i, player in enumerate(PlayerNames):
            psql = 'INSERT INTO players (player_name, team_id) VALUES (%s, %s)'
            mycouser.execute(psql, (player, TeamId))
            mydb.commit()

        # Refresh the treeview after registration
        refresh()
        messagebox.showinfo("Success", "Team and players registered successfully.")
        root.destroy()
    except ValueError:
        messagebox.showerror("Input Error", "Invalid Team ID. It must be a number.")
    except sq.MySQLError as e:
        messagebox.showerror("Database Error", f"Error while interacting with the database: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Run the application
# RegistredTeam()
