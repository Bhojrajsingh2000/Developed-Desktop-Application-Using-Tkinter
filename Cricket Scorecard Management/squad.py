from tkinter import *
from tkinter import messagebox, ttk
import pymysql as sq

# Global variable to store the player ID for update
selected_player_id = None
rightframe = None  # Define rightframe globally

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

def fetch_teams():
    query = "SELECT team_id, team_name FROM teams"
    try:
        mycursor.execute(query)
        teams = mycursor.fetchall()
        return teams
    except sq.Error as e:
        print(f"Error fetching teams: {e}")
        messagebox.showerror("Error", f"Failed to fetch teams: {e}")
        return []

def fetch_team_squad(team_id):
    query = """
     SELECT player_id, player_name
    FROM players
    WHERE team_id = %s
    """
    try:
        mycursor.execute(query, (team_id,))
        squad = mycursor.fetchall()
        return squad
    except sq.Error as e:
        print(f"Error fetching squad: {e}")
        messagebox.showerror("Error", f"Failed to fetch squad: {e}")
        return []

def update_player_name(player_id, new_name):
    try:
        query = "UPDATE players SET player_name = %s WHERE player_id = %s"
        mycursor.execute(query, (new_name, player_id))
        mydb.commit()
        messagebox.showinfo("Success", "Player name updated successfully")
        # After update, refresh the squad display
        refresh_team_squad(get_current_team_id())
    except sq.Error as e:
        print(f"Error updating player name: {e}")
        messagebox.showerror("Error", f"Failed to update player name: {e}")

def delete_player(player_id):
    try:
        # First, delete references in the scores table
        query_scores = "DELETE FROM scores WHERE player_id = %s"
        mycursor.execute(query_scores, (player_id,))
        mydb.commit()
        
        # Then, delete the player
        query = "DELETE FROM players WHERE player_id = %s"
        mycursor.execute(query, (player_id,))
        mydb.commit()
        
        messagebox.showinfo("Success", "Player deleted successfully")
        # After delete, refresh the squad display
        refresh_team_squad(get_current_team_id())
    except sq.Error as e:
        print(f"Error deleting player: {e}")
        messagebox.showerror("Error", f"Failed to delete player: {e}")

def add_new_player(team_id, new_player_name):
    try:
        query = "INSERT INTO players (team_id, player_name) VALUES (%s, %s)"
        mycursor.execute(query, (team_id, new_player_name))
        mydb.commit()
        messagebox.showinfo("Success", "New player added successfully")
        # After insert, refresh the squad display
        refresh_team_squad(team_id)
    except sq.Error as e:
        print(f"Error adding new player: {e}")
        messagebox.showerror("Error", f"Failed to add new player: {e}")

def get_current_team_id():
    # Implement this function to return the current selected team_id
    # Example: return selected_team_id
    pass

def open_update_window(player_id, player_name):
    global selected_player_id
    selected_player_id = player_id
    
    update_window = Toplevel()
    update_window.title("Update Player Name")
    update_window.geometry("400x200")
    
    # Label and Entry for player name
    player_name_label = Label(update_window, text="Player Name:", font=('Arial', 14))
    player_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    
    player_name_entry = Entry(update_window, font=('Arial', 14), width=25)
    player_name_entry.insert(0, player_name)  # Pre-fill current player name
    player_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    
    # Button to update player name
    update_button = Button(update_window, text="Update", font=('Arial', 14), command=lambda: update_player_name(selected_player_id, player_name_entry.get()))
    update_button.grid(row=1, column=0, columnspan=2, pady=10)
    
    update_window.mainloop()

def refresh_team_squad(team_id):
    global rightframe
    for widget in rightframe.winfo_children():
        widget.destroy()
    
    squad = fetch_team_squad(team_id)
    
    # Define column headers
    headers = ['Player ID','Player']
    for i, header in enumerate(headers):
        label = Label(rightframe, text=header, font=('Arial', 14, 'bold'), bg='gray', fg='white')
        label.grid(row=0, column=i, padx=5, pady=5, sticky='ew')
    
    y_position = 1
    if not squad:
        label = Label(rightframe, text="No data found", font=('Arial', 15))
        label.grid(row=y_position, column=0, columnspan=len(headers), pady=5)
    else:
        for player in squad:
            player_id, player_name = player
            
            # Display player details
            for i, detail in enumerate(player):
                label = Label(rightframe, text=f"{detail}", font=('Arial', 14))
                label.grid(row=y_position, column=i, padx=5, pady=5, sticky='ew')
            
            # Update button (opens update window)
            update_button = Button(rightframe, text="Update", font=('Arial', 12), bg='blue', fg='white', command=lambda p_id=player_id, p_name=player_name: open_update_window(p_id, p_name))
            update_button.grid(row=y_position, column=len(headers), padx=5, pady=5, sticky='ew')
            
            # Delete button
            delete_button = Button(rightframe, text="Delete", font=('Arial', 12), bg='red', fg='white', command=lambda p_id=player_id: delete_player(p_id))
            delete_button.grid(row=y_position, column=len(headers)+1, padx=5, pady=5, sticky='ew')
            
            y_position += 1
        
        # Entry for adding a new player
        new_player_label = Label(rightframe, text="New Player Name:", font=('Arial', 12))
        new_player_label.grid(row=y_position, column=0, padx=5, pady=5, sticky='e')
        
        new_player_entry = Entry(rightframe, font=('Arial', 12))
        new_player_entry.grid(row=y_position, column=1, padx=5, pady=5, sticky='w')
        
        add_player_button = Button(rightframe, text="Add Player", font=('Arial', 12), bg='green', fg='white', command=lambda: add_new_player(team_id, new_player_entry.get()))
        add_player_button.grid(row=y_position, column=2, padx=5, pady=5, sticky='ew')
    
    message=Label(rightframe,text='Note : Click on Team Button For Refresh Data',font=('Arial',13),fg='red')
    message.place(x=50, y=900)
def Team():
    root = Tk()
    root.title("Squad")
    root.geometry("1920x1000+0+0")
    root.resizable(0, 0)
    
    # Title window
    titlewindow = Label(root, text='Team Squad', font=('robotic', 20, 'bold'), bg='green', fg='white')
    titlewindow.place(x=0, y=0, width=1920, height=50)
    
    # Left frame
    leftframe = LabelFrame(root, bd=1, relief='solid')
    leftframe.place(x=0, y=50, width=300, height=950)
    
    # Right frame
    global rightframe
    rightframe = LabelFrame(root, bd=1, relief='solid')
    rightframe.place(x=300, y=50, width=1700, height=950)
    
    # Fetch teams from database
    teams = fetch_teams()
    
    # Create a button for each team
    y_position = 5
    for team in teams:
        team_id = team[0]
        team_name = team[1]
        teambtn = Button(leftframe, text=team_name, font=('Arial', 14), bd=1, relief='solid', command=lambda t_id=team_id: refresh_team_squad(t_id))
        teambtn.place(x=5, y=y_position, width=290, height=30)
        y_position += 40
    
    root.mainloop()


