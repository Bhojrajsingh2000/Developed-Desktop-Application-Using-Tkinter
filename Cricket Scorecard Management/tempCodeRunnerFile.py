def fetch_team_name(team_id):
#     try:
#         mycursor.execute("SELECT team_name FROM teams WHERE team_id = %s", (team_id,))
#         team_name = mycursor.fetchone()
#         return team_name[0] if team_name else "Unknown"
#     except sq.Error as e:
#         print(f"Error fetching team name: {e}")
#         messagebox.showerror("Error", f"Failed to fetch team name: {e}")
#         return "Unknown"