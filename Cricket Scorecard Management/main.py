from tkinter import *
from tkinter import messagebox
import pymysql as sq
from datetime import datetime
import registration as rg
import schedule as sd
import squad as qd
import teamRank
import state
import startmatch
# Database connection
mydb = sq.connect(
    host='localhost',
    user='root',
    password='',
    database='cricket'
)
mycursor = mydb.cursor()

def get_todays_matches():
    today = datetime.today().strftime('%Y-%m-%d')
    query = """
    SELECT t1.team_name, t2.team_name
    FROM matches
    JOIN teams t1 ON matches.team1_id = t1.team_id
    JOIN teams t2 ON matches.team2_id = t2.team_id
    WHERE matches.date = %s
    """
    try:
        mycursor.execute(query, (today,))
        matches = mycursor.fetchall()
        return matches
    except sq.Error as e:
        print(f"Error fetching today's matches: {e}")
        messagebox.showerror("Error", f"Failed to fetch today's matches: {e}")
        return []

def refresh_data():
    try:
        # Update total play team
        mycursor.execute("SELECT COUNT(*) FROM teams")
        total_teams = mycursor.fetchone()[0]
        total_teams_label.config(text=f"Total Play Team\n{total_teams}")
       

        # Update total players
        mycursor.execute("SELECT COUNT(*) FROM players")
        total_players = mycursor.fetchone()[0]
        total_players_label.config(text=f"Total Players\n{total_players}")
        

        # Update total matches
        mycursor.execute("SELECT COUNT(*) FROM matches")
        total_matches = mycursor.fetchone()[0]
        total_matches_label.config(text=f"Total Matches\n{total_matches}")
       

        # Update played matches
        mycursor.execute("SELECT COUNT(*) FROM matches WHERE status = 'play'")
        played_matches = mycursor.fetchone()[0]
        played_matches_label.config(text=f"Played Matches\n{played_matches}")
       

        # Update today's matches
        matches = get_todays_matches()
        if matches:
            matches_today = '\n'.join([f"{match[0]} vs {match[1]}" for match in matches])
            todays_matches_label.config(text=f"{matches_today}")
            
        else:
            todays_matches_label.config(text="No matches today")
            start_match.place
            

    except sq.Error as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

    # Schedule the next refresh after 10 seconds (adjust as needed)
    root.after(1000, refresh_data)
    
def match_schedule():
    messagebox.showinfo("Match Schedule", "This feature is under development.")

def team_rank():
    messagebox.showinfo("Team Rank", "This feature is under development.")

def squad():
    messagebox.showinfo("Squad", "This feature is under development.")

def stats():
    messagebox.showinfo("Stats", "This feature is under development.")

    # Create the main window
def main():
    global root,total_teams_label,todays_matches_label,start_match,played_matches_label,total_players_label,total_matches_label
    root = Tk()
    root.title("Cricket Team Management Dashboard")
    root.geometry("1920x1000+0+0")

    # Create and place labels for the dashboard
    titlewindow = Label(root, text='Live Cricket Dashboard', font=('Arial', 20, 'bold'), bg='green', fg='white')
    titlewindow.place(x=20, y=0, width=1880, height=50)
    registrationbtn = Button(root, text='Team Registration', font=('Arial', 12), command=rg.RegistredTeam)
    registrationbtn.place(x=40, y=10, width=200)

    total_teams_label = Label(root, text="Total Play Team", font=('Arial', 30), bg='green', fg='white')
    total_teams_label.place(x=50, y=80, width=400, height=150)

    total_players_label = Label(root, text="Total Players", font=('Arial', 30), bg='green', fg='white')
    total_players_label.place(x=500, y=80, width=400, height=150)

    total_matches_label = Label(root, text="Total Matches", font=('Arial', 30), bg='green', fg='white')
    total_matches_label.place(x=950, y=80, width=400, height=150)

    played_matches_label = Label(root, text="Played Matches", font=('Arial', 30), bg='green', fg='white')
    played_matches_label.place(x=1400, y=80, width=400, height=150)

    matchlb = Label(root, text='Today Match', bg='orange', fg='white', font=('Arial', 20))
    matchlb.place(x=20, y=250, width=1880, height=50)

    date = Label(root, text=f"Date: {datetime.today().strftime('%d / %m / %Y')}", font=('Arial', 20))
    date.place(x=20, y=325, height=50)
    todays_matches_label = Label(root, text="", font=('Arial', 20))
    todays_matches_label.place(x=700, y=325, width=400, height=50)

    start_match = Button(root, text="Start Match", font=('Arial', 20), bg='blue', fg='white', command=startmatch.MatchStart)
    start_match.place(x=1400, y=325, width=300, height=50)

    refresh_button = Button(root, text="Refresh", command=refresh_data)
    refresh_button.place(x=1750, y=10, width=100)
    refresh_button1 = Button(root, text="Refresh", command=refresh_data1)
    refresh_button1.place(x=1750, y=10, width=100)

    controlboard = Label(root, text='Control Board', bg='orange', fg='white', font=('Arial', 20))
    controlboard.place(x=20, y=400, width=1880, height=50)

    # Add buttons for additional features
    match_schedule_button = Button(root, text="Match Schedule", font=('Arial', 20), bg='blue', fg='white', command=sd.schedule)
    match_schedule_button.place(x=50, y=500, width=400, height=50)

    team_rank_button = Button(root, text="Team Rank", font=('Arial', 20), bg='blue', fg='white', command=teamRank.TeamRank)
    team_rank_button.place(x=500, y=500, width=400, height=50)

    squad_button = Button(root, text="Squad", font=('Arial', 20), bg='blue', fg='white', command=qd.Team)
    squad_button.place(x=950, y=500, width=400, height=50)

    stats_button = Button(root, text="Stats", font=('Arial', 20), bg='blue', fg='white', command=state.State)
    stats_button.place(x=1400, y=500, width=400, height=50)

        # Initial refresh to populate data
    refresh_data()

    # Run the main loop
    root.mainloop()
def refresh_data1():
    root.destroy()
    main()
main()


