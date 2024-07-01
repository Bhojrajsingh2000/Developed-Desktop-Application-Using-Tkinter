from tkinter import *
from tkinter import messagebox
import pymysql as sq

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

def fetch_team_rankings():
    query = """
    SELECT team_id, team_name, matches, wins, loss, no_result, point, net_run_rate
    FROM team_rankings
    ORDER BY point DESC, net_run_rate DESC
    """
    try:
        mycursor.execute(query)
        rankings = mycursor.fetchall()
        return rankings
    except sq.Error as e:
        print(f"Error fetching team rankings: {e}")
        messagebox.showerror("Error", f"Failed to fetch team rankings: {e}")
        return []

def TeamRank():
    root = Tk()
    root.title("Team Rank")
    root.geometry("1350x750+0+0")
    root.configure(background="white")
    root.resizable(False, False)

    # Title window
    titlewindow = Label(root, text='Team Rank', font=('robotic', 20, 'bold'), bg='green', fg='white')
    titlewindow.place(x=10, y=0, width=1330, height=50)
    
    # Header labels
    headers = ['Team Id', 'Team', 'Matches', 'Wins', 'Losses', 'No Result', 'Points', 'Net Run Rate']
    for i, header in enumerate(headers):
        label = Label(root, text=header, font=('Arial', 15), bg='green', fg='white')
        label.place(x=10 + i*166, y=60, width=166, height=30)
    
    # Fetch team rankings from database
    rankings = fetch_team_rankings()

    # Check if there are any rankings returned
    if not rankings:
        no_data_label = Label(root, text="No Data Found", font=('Arial', 15), bg='white', fg='red')
        no_data_label.place(x=10, y=100, width=1330, height=30)
    else:
        # Display team rankings
        y_position = 100  # Initial vertical position for the first row of data
        for ranking in rankings:
            for i, data in enumerate(ranking):
                label = Label(root, text=str(data), font=('Arial', 15), bg='white', fg='black', borderwidth=2, relief="solid")
                label.place(x=10 + i*166, y=y_position, width=166, height=30)
            y_position += 40  # Update vertical position for the next row of data
    
    root.mainloop()


