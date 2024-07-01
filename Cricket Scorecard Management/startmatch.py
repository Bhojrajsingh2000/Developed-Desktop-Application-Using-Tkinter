from tkinter import *
from tkinter import ttk
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

def fetch_teams():
    query = "SELECT team_name FROM teams"
    try:
        mycursor.execute(query)
        teams = mycursor.fetchall()
        return [team[0] for team in teams]
        
    except sq.Error as e:
        print(f"Error fetching teams: {e}")
        messagebox.showerror("Error", f"Failed to fetch teams: {e}")
        return []

def fetch_players(team_name):
    query = "SELECT player_name FROM players inner join teams on players.team_id = teams.team_id WHERE teams.team_name = %s"
    try:
        mycursor.execute(query, (team_name,))
        players = mycursor.fetchall()
        return [player[0] for player in players]
    except sq.Error as e:
        print(f"Error fetching players: {e}")
        messagebox.showerror("Error", f"Failed to fetch players: {e}")
        return []
    
class MatchStart():
    def __init__(self):
        self.root = Tk()
        self.root.title("Cricket Score Project")
        self.root.geometry("1920x1000+0+0")
        self.root.resizable(False, False)

        # Title
        titlelb = Label(self.root, text='Live Cricket Score Manage System', font=('robotic', 20), bg='green', fg='white')
        titlelb.place(x=10, y=0, width=1900, height=50)

        # Change Inning button
        changeInningbtn = Button(self.root, text='Change Innings', font=('robotic', 14), bg='gray', fg='white', bd=1, relief='solid')
        changeInningbtn.place(x=30, y=5)
        refreshbtn = Button(self.root, text='Refresh', font=('robotic', 14), bg='gray', fg='white', bd=1, relief='solid')
        refreshbtn.place(x=1800, y=5)

        # Team selection
        self.titleslb = Label(self.root, text=f'Batting\t\t\t\t\t\t\t\t\t\tBowlling', font=('robotic', 20))
        self.titleslb.place(x=30, y=60)
        self.teams = fetch_teams()
        self.teamNamecombo = ttk.Combobox(self.root, values=self.teams, font=('robotic', 15), state='readonly')
        self.teamNamecombo.place(x=30, y=100, width=200)
        self.teamNamecombo1 = ttk.Combobox(self.root, values=self.teams, font=('robotic', 15), state='readonly')
        self.teamNamecombo1.place(x=1100, y=100, width=200)
        
        self.fetchplayer=Button(self.root,text='Fetch Players list',bd=1,relief='solid', command=self.fetch_players_list)
        self.fetchplayer.place(x=30, y=140,width=150)
        self.fetchplayer1=Button(self.root,text='Fetch Players list',bd=1,relief='solid', command=self.fetch_players_list1)
        self.fetchplayer1.place(x=1100, y=140,width=150)
        #score and wicket
        self.score = Label(self.root, text=f'0/0', font=('robotic', 45))
        self.score.place(x=350, y=100)
        self.over=Label(self.root,text=f'O :(0.0)',font=('robotic', 15))
        self.over.place(x=250, y=150)
        self.runrate=Label(self.root,text=f'RR : 13.5',font=('robotic', 15))
        self.runrate.place(x=470, y=150)
        #============================================================================
        self.label=Label(self.root,text='Player\t\t\tRun\tBall\t1\t2\t3\t4\t6\tBalls\t Status\t\tBowler',font=('robotic', 15))
        self.label.place(x=20,y=200)
        #================================================================
        self.batter1=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter1.place(x=20,y=240,width=210)
        self.run1=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run1.place(x=290,y=240)
        #----------------------------------------------------------------
        self.btn1_1=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function1(1))
        self.btn1_1.place(x=450,y=240,width=40,height=30)
        self.btn2_1=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function1(2))
        self.btn2_1.place(x=540,y=240,width=40,height=30)
        self.btn3_1=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function1(3))
        self.btn3_1.place(x=625,y=240,width=40,height=30)
        self.btn4_1=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function1(4))
        self.btn4_1.place(x=710,y=240,width=40,height=30)
        self.btn6_1=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function1(6))
        self.btn6_1.place(x=800,y=240,width=40,height=30)
        self.btn7_1=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function1(0))
        self.btn7_1.place(x=900,y=240,width=50,height=30)
        self.btn8_1=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionA(0))
        self.btn8_1.place(x=1000,y=240,width=50,height=30)
        
        self.batter2=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter2.place(x=20,y=280,width=210)
        self.run2=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run2.place(x=290,y=280)
        #----------------------------------------------------------------
        self.btn1_2=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function2(1))
        self.btn1_2.place(x=450,y=280,width=40,height=30)
        self.btn2_2=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function2(2))
        self.btn2_2.place(x=540,y=280,width=40,height=30)
        self.btn3_2=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function2(3))
        self.btn3_2.place(x=625,y=280,width=40,height=30)
        self.btn4_2=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function2(4))
        self.btn4_2.place(x=710,y=280,width=40,height=30)
        self.btn6_2=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function2(6))
        self.btn6_2.place(x=800,y=280,width=40,height=30)
        self.btn7_2=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function2(0))
        self.btn7_2.place(x=900,y=280,width=50,height=30)
        self.btn8_2=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionB(0))
        self.btn8_2.place(x=1000,y=280,width=50,height=30)
        #--------------------------------------------------------
        self.batter3=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter3.place(x=20,y=320,width=210)
        self.run3=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run3.place(x=290,y=320)
        #----------------------------------------------------------------
        self.btn1_3=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function3(1))
        self.btn1_3.place(x=450,y=320,width=40,height=30)
        self.btn2_3=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function3(2))
        self.btn2_3.place(x=540,y=320,width=40,height=30)
        self.btn3_3=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function3(3))
        self.btn3_3.place(x=625,y=320,width=40,height=30)
        self.btn4_3=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function3(4))
        self.btn4_3.place(x=710,y=320,width=40,height=30)
        self.btn6_3=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function3(6))
        self.btn6_3.place(x=800,y=320,width=40,height=30)
        self.btn7_3=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function3(0))
        self.btn7_3.place(x=900,y=320,width=50,height=30)
        self.btn8_3=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionC(0))
        self.btn8_3.place(x=1000,y=320,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter4=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter4.place(x=20,y=360,width=210)
        self.run4=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run4.place(x=290,y=360)
        #----------------------------------------------------------------
        self.btn1_4=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function4(1))
        self.btn1_4.place(x=450,y=360,width=40,height=30)
        self.btn2_4=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function4(2))
        self.btn2_4.place(x=540,y=360,width=40,height=30)
        self.btn3_4=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function4(3))
        self.btn3_4.place(x=625,y=360,width=40,height=30)
        self.btn4_4=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function4(4))
        self.btn4_4.place(x=710,y=360,width=40,height=30)
        self.btn6_4=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function4(6))
        self.btn6_4.place(x=800,y=360,width=40,height=30)
        self.btn7_4=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function4(0))
        self.btn7_4.place(x=900,y=360,width=50,height=30)
        self.btn8_4=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionD(0))
        self.btn8_4.place(x=1000,y=360,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter5=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter5.place(x=20,y=400,width=210)
        self.run5=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run5.place(x=290,y=400)
                #----------------------------------------------------------------
        self.btn1_5=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function5(1))
        self.btn1_5.place(x=450,y=400,width=40,height=30)
        self.btn2_5=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function5(2))
        self.btn2_5.place(x=540,y=400,width=40,height=30)
        self.btn3_5=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function5(3))
        self.btn3_5.place(x=625,y=400,width=40,height=30)
        self.btn4_5=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function5(4))
        self.btn4_5.place(x=710,y=400,width=40,height=30)
        self.btn6_5=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function5(6))
        self.btn6_5.place(x=800,y=400,width=40,height=30)
        self.btn7_5=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function5(0))
        self.btn7_5.place(x=900,y=400,width=50,height=30)
        self.btn8_5=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionE(0))
        self.btn8_5.place(x=1000,y=400,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter6=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter6.place(x=20,y=440,width=210)
        self.run6=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run6.place(x=290,y=440)
                #----------------------------------------------------------------
        self.btn1_6=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function6(1))
        self.btn1_6.place(x=450,y=440,width=40,height=30)
        self.btn2_6=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function6(2))
        self.btn2_6.place(x=540,y=440,width=40,height=30)
        self.btn3_6=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function6(3))
        self.btn3_6.place(x=625,y=440,width=40,height=30)
        self.btn4_6=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function6(4))
        self.btn4_6.place(x=710,y=440,width=40,height=30)
        self.btn6_6=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function6(6))
        self.btn6_6.place(x=800,y=440,width=40,height=30)
        self.btn7_6=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function6(0))
        self.btn7_6.place(x=900,y=440,width=50,height=30)
        self.btn8_6=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionF(0))
        self.btn8_6.place(x=1000,y=440,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter7=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter7.place(x=20,y=480,width=210)
        self.run7=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run7.place(x=290,y=480)
                #----------------------------------------------------------------
        self.btn1_7=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function7(1))
        self.btn1_7.place(x=450,y=480,width=40,height=30)
        self.btn2_7=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function7(2))
        self.btn2_7.place(x=540,y=480,width=40,height=30)
        self.btn3_7=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function7(3))
        self.btn3_7.place(x=625,y=480,width=40,height=30)
        self.btn4_7=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function7(4))
        self.btn4_7.place(x=710,y=480,width=40,height=30)
        self.btn6_7=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function7(6))
        self.btn6_7.place(x=800,y=480,width=40,height=30)
        self.btn7_7=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function7(0))
        self.btn7_7.place(x=900,y=480,width=50,height=30)
        self.btn8_7=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionG(0))
        self.btn8_7.place(x=1000,y=480,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter8=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter8.place(x=20,y=520,width=210)
        self.run8=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run8.place(x=290,y=520)
                #----------------------------------------------------------------
        self.btn1_8=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function8(1))
        self.btn1_8.place(x=450,y=520,width=40,height=30)
        self.btn2_8=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function8(2))
        self.btn2_8.place(x=540,y=520,width=40,height=30)
        self.btn3_8=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function8(3))
        self.btn3_8.place(x=625,y=520,width=40,height=30)
        self.btn4_8=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function8(4))
        self.btn4_8.place(x=710,y=520,width=40,height=30)
        self.btn6_8=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function8(6))
        self.btn6_8.place(x=800,y=520,width=40,height=30)
        self.btn7_8=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function8(0))
        self.btn7_8.place(x=900,y=520,width=50,height=30)
        self.btn8_8=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionH(0))
        self.btn8_8.place(x=1000,y=520,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter9=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter9.place(x=20,y=560,width=210)
        self.run9=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run9.place(x=290,y=560)
                #----------------------------------------------------------------
        self.btn1_9=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function9(1))
        self.btn1_9.place(x=450,y=560,width=40,height=30)
        self.btn2_9=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function9(2))
        self.btn2_9.place(x=540,y=560,width=40,height=30)
        self.btn3_9=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function9(3))
        self.btn3_9.place(x=625,y=560,width=40,height=30)
        self.btn4_9=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function9(4))
        self.btn4_9.place(x=710,y=560,width=40,height=30)
        self.btn6_9=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function9(6))
        self.btn6_9.place(x=800,y=560,width=40,height=30)
        self.btn7_9=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function9(0))
        self.btn7_9.place(x=900,y=560,width=50,height=30)
        self.btn8_9=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionI(0))
        self.btn8_9.place(x=1000,y=560,width=50,height=30)
        #--------------------------------------------------------
        self.batter10=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter10.place(x=20,y=600,width=210)
        self.run10=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run10.place(x=290,y=600)
                #----------------------------------------------------------------
        self.btn1_10=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function10(1))
        self.btn1_10.place(x=450,y=600,width=40,height=30)
        self.btn2_10=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function10(2))
        self.btn2_10.place(x=540,y=600,width=40,height=30)
        self.btn3_10=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function10(3))
        self.btn3_10.place(x=625,y=600,width=40,height=30)
        self.btn4_10=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function10(4))
        self.btn4_10.place(x=710,y=600,width=40,height=30)
        self.btn6_10=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function10(6))
        self.btn6_10.place(x=800,y=600,width=40,height=30)
        self.btn7_10=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function10(0))
        self.btn7_10.place(x=900,y=600,width=50,height=30)
        self.btn8_10=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionJ(0))
        self.btn8_10.place(x=1000,y=600,width=50,height=30)
        #--------------------------------------------------------
        
        self.batter11=ttk.Combobox(self.root,font=('robotic', 15),state='r')
        self.batter11.place(x=20,y=640,width=210)
        self.run11=Label(self.root,text=f'0\t0',font=('robotic', 15))
        self.run11.place(x=290,y=640)
                #----------------------------------------------------------------
        self.btn1_11=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function11(1))
        self.btn1_11.place(x=450,y=640,width=40,height=30)
        self.btn2_11=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function11(2))
        self.btn2_11.place(x=540,y=640,width=40,height=30)
        self.btn3_11=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function11(3))
        self.btn3_11.place(x=625,y=640,width=40,height=30)
        self.btn4_11=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function11(4))
        self.btn4_11.place(x=710,y=640,width=40,height=30)
        self.btn6_11=Button(self.root,text=f'0',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function11(6))
        self.btn6_11.place(x=800,y=640,width=40,height=30)
        self.btn7_11=Button(self.root,text=f'DOT',font=('robotic', 12),bd=1,relief='solid',command=lambda: self.some_function11(0))
        self.btn7_11.place(x=900,y=640,width=50,height=30)
        self.btn8_11=Button(self.root,text=f'OUT',font=('robotic', 12),bg='red',fg='white',bd=1,relief='solid',command=lambda: self.some_functionK(0))
        self.btn8_11.place(x=1000,y=640,width=50,height=30)
        self.lockButton=Button(self.root,text=f'Lock Players Order',font=('robotic', 12),bg='blue',fg='white',bd=1,relief='solid',command=self.lockPlayers)
        self.lockButton.place(x=700,y=840,width=200,height=40)
        #--------------------------------------------------------
        
        #++++++++++++++++++++++++++++++++,command=lambda: self.some_function11(0)++++++++++++++++++++++++Bowler++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.bowler1=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler1.place(x=1100,y=240,width=200)
       
        #--------------------------------------------------------
        self.bowler2=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler2.place(x=1100,y=280,width=200)
        
        #--------------------------------------------------------
        self.bowler3=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler3.place(x=1100,y=320,width=200)
        
        #--------------------------------------------------------
        self.bowler4=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler4.place(x=1100,y=360,width=200)
        
        #--------------------------------------------------------
        self.bowler5=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler5.place(x=1100,y=400,width=200)
        
        #--------------------------------------------------------
        self.bowler6=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler6.place(x=1100,y=440,width=200)
       
        #--------------------------------------------------------
        self.bowler7=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler7.place(x=1100,y=480,width=200)
        
        #--------------------------------------------------------
        self.bowler8=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler8.place(x=1100,y=520,width=200)
        
        #--------------------------------------------------------
        self.bowler9=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler9.place(x=1100,y=560,width=200)
        
        #--------------------------------------------------------
        self.bowler10=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler10.place(x=1100,y=600,width=200)
        
        #--------------------------------------------------------
        self.bowler11=ttk.Combobox(self.root,font=('robotic', 15),state='readonly')
        self.bowler11.place(x=1100,y=640,width=200)
        
        #--------------------------------------------------------
        self.savedata=Button(self.root,text='Sumbit Data',font=('robotic', 12),bd=1,relief='solid',bg='green',fg='white')
        self.savedata.place(x=1070,y=840,width=200,height=40)
        self.root.mainloop()
    def lockPlayers(self):
        self.batter1.config(state='disabled')
        self.batter2.config(state='disabled')
        self.batter3.config(state='disabled')
        self.batter4.config(state='disabled')
        self.batter5.config(state='disabled')
        self.batter6.config(state='disabled')
        self.batter7.config(state='disabled')
        self.batter8.config(state='disabled')
        self.batter9.config(state='disabled')
        self.batter10.config(state='disabled')
        self.batter11.config(state='disabled')
        self.lockButton.config(state='disabled')
        self.bowler1.config(state='disabled')
        self.bowler2.config(state='disabled')
        self.bowler3.config(state='disabled')
        self.bowler4.config(state='disabled')
        self.bowler5.config(state='disabled')
        self.bowler6.config(state='disabled')
        self.bowler7.config(state='disabled')
        self.bowler8.config(state='disabled')
        self.bowler9.config(state='disabled')
        self.bowler10.config(state='disabled')
        self.bowler11.config(state='disabled')
        self.teamNamecombo1.config(state='disabled')
        self.fetchplayer1.config(state='disabled')
        self.teamNamecombo.config(state='disabled')
        self.fetchplayer.config(state='disabled')

    def fetch_players_list(self):
        team_name = self.teamNamecombo.get()
        self.players = fetch_players(team_name)
        self.batter1['values'] = self.players
        self.batter2['values'] = self.players
        self.batter3['values'] = self.players
        self.batter4['values'] = self.players
        self.batter5['values'] = self.players
        self.batter6['values'] = self.players
        self.batter7['values'] = self.players
        self.batter8['values'] = self.players
        self.batter9['values'] = self.players
        self.batter10['values'] = self.players
        self.batter11['values'] = self.players
        
    def fetch_players_list1(self):
        team_name = self.teamNamecombo1.get()
        self.players1 = fetch_players(team_name)
        self.bowler1['values'] = self.players1
        self.bowler2['values'] = self.players1
        self.bowler3['values'] = self.players1
        self.bowler4['values'] = self.players1
        self.bowler5['values'] = self.players1
        self.bowler6['values'] = self.players1
        self.bowler7['values'] = self.players1
        self.bowler8['values'] = self.players1
        self.bowler9['values'] = self.players1
        self.bowler10['values'] = self.players1
        self.bowler11['values'] = self.players1
        
    total_run=0
    total_balls=0
    runs1=0
    balls1=0
    wickets=0
    one1,two1,three1,four1,six1=0,0,0,0,0
    def some_function1(self,value):
        
        self.runs1+= value
        self.balls1+=1
        self.total_run+=value
        self.total_balls+=1
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
            
            
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run1.config(text=f'{self.runs1}\t{self.balls1}')
       
        if value==1:
            self.one1+=1
            self.btn1_1.config(text=f'{self.one1}')
        elif value==2:
            self.two1+=1
            self.btn2_1.config(text=f'{self.two1}')
        elif value==3:
            self.three1+=1
            self.btn3_1.config(text=f'{self.three1}')
        elif value==4:
            self.four1+=1
            self.btn4_1.config(text=f'{self.four1}')
        elif value==6:
            self.six1+=1
            self.btn6_1.config(text=f'{self.six1}')
        elif value==0:
            self.balls1+=1
            self.run1.config(text=f'{self.runs}\t{self.balls1}')
        
    runs2=0
    balls2=0
    one2, two2, three2, four2, six2=0,0,0,0,0
    def some_function2(self,value):
        
        self.runs2+= value
        self.balls2+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run2.config(text=f'{self.runs2}\t{self.balls2}')
        
        if value==1:
            self.one2+=1
            self.btn1_2.config(text=f'{self.one2}')
        elif value==2:
            self.two2+=1
            self.btn2_2.config(text=f'{self.two2}')
        elif value==3:
            self.three2+=1
            self.btn3_2.config(text=f'{self.three2}')
        elif value==4:
            self.four2+=1
            self.btn4_2.config(text=f'{self.four2}')
        elif value==6:
            self.six2+=1
            self.btn6_2.config(text=f'{self.six2}')
        elif value==0:
            self.balls2+=1
            self.run1.config(text=f'{self.runs2}\t{self.balls2}')
    runs3=0
    balls3=0
    one3,two3,three3,four3,six3=0,0,0,0,0
    def some_function3(self,value):
        self.runs3+=value
        self.balls3+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run3.config(text=f'{self.runs3}\t{self.balls3}')
       
        if value==1:
            self.one3+=1
            self.btn1_3.config(text=f'{self.one3}')
        elif value==2:
            self.two3+=1
            self.btn2_3.config(text=f'{self.two3}')
        elif value==3:
            self.three3+=1
            self.btn3_3.config(text=f'{self.three3}')
        elif value==4:
            self.four3+=1
            self.btn4_3.config(text=f'{self.four3}')
        elif value==6:
            self.six3+=1
            self.btn6_3.config(text=f'{self.six3}')
        elif value==0:
            self.balls3+=1
            self.run1.config(text=f'{self.runs4}\t{self.balls3}')
    runs4=0
    balls4=0
    one4,two4,three4,four4,six4=0,0,0,0,0
    def some_function4(self,value):
        self.runs4+=value
        self.balls4+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run4.config(text=f'{self.runs4}\t{self.balls4}')
       
        if value==1:
            self.one4+=1
            self.btn1_4.config(text=f'{self.one4}')
        elif value==2:
            self.two4+=1
            self.btn2_4.config(text=f'{self.two4}')
        elif value==3:
            self.three4+=1
            self.btn3_4.config(text=f'{self.three4}')
        elif value==4:
            self.four4+=1
            self.btn4_4.config(text=f'{self.four4}')
        elif value==6:
            self.six4+=1
            self.btn6_4.config(text=f'{self.six4}')
        elif value==0:
            self.balls4+=1
            self.run1.config(text=f'{self.runs4}\t{self.balls4}')
    runs5=0
    balls5=0
    one5,two5,three5,four5,six5=0,0,0,0,0
    def some_function5(self,value):
        self.runs5+=value
        self.balls5+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run5.config(text=f'{self.runs5}\t{self.balls5}')
        
        if value==1:
            self.one5+=1
            self.btn1_5.config(text=f'{self.one5}')
        elif value==2:
            self.two5+=1
            self.btn2_5.config(text=f'{self.two5}')
        elif value==3:
            self.three5+=1
            self.btn3_5.config(text=f'{self.three5}')
        elif value==4:
            self.four5+=1
            self.btn4_5.config(text=f'{self.four5}')
        elif value==6:
            self.six5+=1
            self.btn6_5.config(text=f'{self.six5}')
        elif value==0:
            self.balls5+=1
            self.run1.config(text=f'{self.runs5}\t{self.balls5}')
    runs6=0
    balls6=0
    one6,two6,three6,four6,six6=0,0,0,0,0
    def some_function6(self,value):
        self.runs6+=value
        self.balls6+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run6.config(text=f'{self.runs6}\t{self.balls6}')
       
        if value==1:
            self.one6+=1
            self.btn1_6.config(text=f'{self.one6}')
        elif value==2:
            self.two6+=1
            self.btn2_6.config(text=f'{self.two6}')
        elif value==3:
            self.three6+=1
            self.btn3_6.config(text=f'{self.three6}')
        elif value==4:
            self.four6+=1
            self.btn4_6.config(text=f'{self.four6}')
        elif value==6:
            self.six6+=1
            self.btn6_6.config(text=f'{self.six6}')
        elif value==0:
            self.balls6+=1
            self.run1.config(text=f'{self.runs6}\t{self.balls6}')
    runs7=0
    balls7=0
    one7,two7,three7,four7,six7=0,0,0,0,0
    def some_function7(self,value):
        self.runs7+=value
        self.balls7+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run7.config(text=f'{self.runs7}\t{self.balls7}')
        
        if value==1:
            self.one7+=1
            self.btn1_7.config(text=f'{self.one7}')
        elif value==2:
            self.two7+=1
            self.btn2_7.config(text=f'{self.two7}')
        elif value==3:
            self.three7+=1
            self.btn3_7.config(text=f'{self.three7}')
        elif value==4:
            self.four7+=1
            self.btn4_7.config(text=f'{self.four7}')
        elif value==6:
            self.six7+=1
            self.btn6_7.config(text=f'{self.six7}')
        elif value==0:
            self.balls7+=1
            self.run1.config(text=f'{self.runs7}\t{self.balls7}')
    runs8=0
    balls8=0
    one8,two8,three8,four8,six8=0,0,0,0,0
    def some_function8(self,value):
        self.runs8+=value
        self.balls8+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run8.config(text=f'{self.runs8}\t{self.balls8}')
       
        if value==1:
            self.one8+=1
            self.btn1_8.config(text=f'{self.one8}')
        elif value==2:
            self.two8+=1
            self.btn2_8.config(text=f'{self.two8}')
        elif value==3:
            self.three8+=1
            self.btn3_8.config(text=f'{self.three8}')
        elif value==4:
            self.four8+=1
            self.btn4_8.config(text=f'{self.four8}')
        elif value==6:
            self.six8+=1
            self.btn6_8.config(text=f'{self.six8}')
        elif value==0:
            self.balls8+=1
            self.run1.config(text=f'{self.runs8}\t{self.balls8}')
        
            
    runs9=0
    balls9=0
    one9,two9,three9,four9,six9=0,0,0,0,0
    def some_function9(self,value):
        self.runs9+=value
        self.balls9+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
            self.current_over+=self.total_balls//6
            self.total_balls = 0
            self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
            self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
                self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run9.config(text=f'{self.runs9}\t{self.balls9}')
        
        if value==1:
            self.one9+=1
            self.btn1_9.config(text=f'{self.one9}')
        elif value==2:
            self.two9+=1
            self.btn2_9.config(text=f'{self.two9}')
        elif value==3:
            self.three9+=1
            self.btn3_9.config(text=f'{self.three9}')
        elif value==4:
            self.four9+=1
            self.btn4_9.config(text=f'{self.four9}')
        elif value==6:
            self.six9+=1
            self.btn6_9.config(text=f'{self.six9}')
        elif value==0:
            self.balls9+=1
            self.run1.config(text=f'{self.runs9}\t{self.balls9}')
    runs10=0
    balls10=0
    one10,two10,three10,four10,six10=0,0,0,0,0
    def some_function10(self,value):
        self.runs10+=value
        self.balls10+=1
        self.total_run+=value
        self.total_balls+=1
        
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        if self.total_balls==6:
                self.current_over+=self.total_balls//6
                self.total_balls = 0
                self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
                self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run10.config(text=f'{self.runs10}\t{self.balls10}')
       
        if value==1:
            self.one10+=1
            self.btn1_10.config(text=f'{self.one10}')
        elif value==2:
            self.two10+=1
            self.btn2_10.config(text=f'{self.two10}')
        elif value==3:
            self.three10+=1
            self.btn3_10.config(text=f'{self.three10}')
        elif value==4:
            self.four10+=1
            self.btn4_10.config(text=f'{self.four10}')
        elif value==6:
            self.six10+=1
            self.btn6_10.config(text=f'{self.six10}')
        elif value==0:
            self.balls10+=1
            self.run1.config(text=f'{self.runs10}\t{self.balls10}')
    runs11=0
    balls11=0
    current_over=0
    one11,two11,three11,four11,six11=0,0,0,0,0
    def some_function11(self,value):
        self.runs11+=value
        self.balls11+=1
        self.total_run+=value
        self.total_balls+=1
        self.score.config(text=f'{self.total_run}/{self.wickets}')
        
        if self.total_balls==6:
                self.current_over+=self.total_balls//6
                self.total_balls = 0
                self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
        else:
                self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
        self.run11.config(text=f'{self.runs11}\t{self.balls11}')
       
        if value==1:
            self.one11+=1
            self.btn1_11.config(text=f'{self.one11}')
        elif value==2:
            self.two11+=1
            self.btn2_11.config(text=f'{self.two11}')
        elif value==3:
            self.three11+=1
            self.btn3_11.config(text=f'{self.three11}')
        elif value==4:
            self.four11+=1
            self.btn4_11.config(text=f'{self.four11}')
        elif value==6:
            self.six11+=1
            self.btn6_11.config(text=f'{self.six11}')
        elif value==0:
            self.balls11+=1
            self.run1.config(text=f'{self.runs11}\t{self.balls11}')
    
    
    def some_functionA(self, values):
        # ...
        if self.wickets<10:
            if values == 0:  # OUT button
                self.wickets += 1
                self.total_balls += 1
                self.balls1 += 1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run1.config(text=f'{self.runs1}\t{self.balls1}')
                self.btn1_1.config(state='disabled')
                self.btn2_1.config(state='disabled')
                self.btn3_1.config(state='disabled')
                self.btn4_1.config(state='disabled')
                self.btn6_1.config(state='disabled')
                self.btn7_1.config(state='disabled')
                self.btn8_1.config(state='disabled')
        
        try:
            sql = 'INSERT INTO scorcard (player_name, team_name, runs, balls,outby) VALUES (%s, %s, %s, %s, %s)'
            values = (self.batter1.get(), self.teamNamecombo.get(), self.runs1, self.balls1,self.bowler1.get())
            mycursor.execute(sql, values)
            mydb.commit()
            print("Player inserted successfully")
        except sq.Error as e:
            print(f"Error inserting player: {e}")
            # ...
    def some_functionB(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls2 += 1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run2.config(text=f'{self.runs2}\t{self.balls2}')
                self.btn1_2.config(state='disabled')
                self.btn2_2.config(state='disabled')
                self.btn3_2.config(state='disabled')
                self.btn4_2.config(state='disabled')
                self.btn6_2.config(state='disabled')
                self.btn7_2.config(state='disabled')
                self.btn8_2.config(state='disabled')
            sql='insert into scores(player_name,team_id,runs,balls,wicket) Values(%s,%s,%s,%s,%s)'
            mycursor.execute(sql,(self.batter2.get(),1,self.run2,self,self.w1_2))
            mydb.commit()
    def some_functionC(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls3+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run3.config(text=f'{self.runs3}\t{self.balls3}')
                self.btn1_3.config(state='disabled')
                self.btn2_3.config(state='disabled')
                self.btn3_3.config(state='disabled')
                self.btn4_3.config(state='disabled')
                self.btn6_3.config(state='disabled')
                self.btn7_3.config(state='disabled')
                self.btn8_3.config(state='disabled')
    def some_functionD(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls4+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run4.config(text=f'{self.runs4}\t{self.balls4}')
                self.btn1_4.config(state='disabled')
                self.btn2_4.config(state='disabled')
                self.btn3_4.config(state='disabled')
                self.btn4_4.config(state='disabled')
                self.btn6_4.config(state='disabled')
                self.btn7_4.config(state='disabled')
                self.btn8_4.config(state='disabled')
    def some_functionE(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls5+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run5.config(text=f'{self.runs5}\t{self.balls5}')
                self.btn1_5.config(state='disabled')
                self.btn2_5.config(state='disabled')
                self.btn3_5.config(state='disabled')
                self.btn4_5.config(state='disabled')
                self.btn6_5.config(state='disabled')
                self.btn7_5.config(state='disabled')
                self.btn8_5.config(state='disabled')
    def some_functionF(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls6+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run6.config(text=f'{self.runs6}\t{self.balls6}')
                self.btn1_6.config(state='disabled')
                self.btn2_6.config(state='disabled')
                self.btn3_6.config(state='disabled')
                self.btn4_6.config(state='disabled')
                self.btn6_6.config(state='disabled')
                self.btn7_6.config(state='disabled')
                self.btn8_6.config(state='disabled')
    def some_functionG(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls7+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run7.config(text=f'{self.runs7}\t{self.balls7}')
                self.btn1_7.config(state='disabled')
                self.btn2_7.config(state='disabled')
                self.btn3_7.config(state='disabled')
                self.btn4_7.config(state='disabled')
                self.btn6_7.config(state='disabled')
                self.btn7_7.config(state='disabled')
                self.btn8_7.config(state='disabled')
    def some_functionH(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls8+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run8.config(text=f'{self.runs8}\t{self.balls8}')
                self.btn1_8.config(state='disabled')
                self.btn2_8.config(state='disabled')
                self.btn3_8.config(state='disabled')
                self.btn4_8.config(state='disabled')
                self.btn6_8.config(state='disabled')
                self.btn7_8.config(state='disabled')
                self.btn8_8.config(state='disabled')
    def some_functionI(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets += 1
                self.total_balls += 1
                self.balls9+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run9.config(text=f'{self.runs9}\t{self.balls9}')
                self.btn1_9.config(state='disabled')
                self.btn2_9.config(state='disabled')
                self.btn3_9.config(state='disabled')
                self.btn4_9.config(state='disabled')
                self.btn6_9.config(state='disabled')
                self.btn7_9.config(state='disabled')
                self.btn8_9.config(state='disabled')
    def some_functionJ(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets+=1
                self.total_balls += 1
                self.balls10+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run10.config(text=f'{self.runs10}\t{self.balls10}')
                self.btn1_10.config(state='disabled')
                self.btn2_10.config(state='disabled')
                self.btn3_10.config(state='disabled')
                self.btn4_10.config(state='disabled')
                self.btn6_10.config(state='disabled')
                self.btn7_10.config(state='disabled')
                self.btn8_10.config(state='disabled')
    def some_functionK(self,values):
        if self.wickets<10:
            if values == 0:
                self.wickets+=1
                self.total_balls += 1
                self.balls11+=1
                if self.total_balls==6:
                    self.current_over+=self.total_balls//6
                    self.total_balls = 0
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                    self.runrate.config(text=f'RR: {self.total_run//self.current_over}')
                else:
                    self.over.config(text=f'O: {self.current_over}.{self.total_balls}')
                self.score.config(text=f'{self.total_run}/{self.wickets}')
                self.run11.config(text=f'{self.runs11}\t{self.balls11}')
                self.btn1_11.config(state='disabled')
                self.btn2_11.config(state='disabled')
                self.btn3_11.config(state='disabled')
                self.btn4_11.config(state='disabled')
                self.btn6_11.config(state='disabled')
                self.btn7_11.config(state='disabled')
                self.btn8_11.config(state='disabled')
    y1=0
    def bowler_function1(self,x):
        self.y1+=x
        self.w1_1.config(text=f'{self.y1}')
    y2=0
    def bowler_function2(self,x):
        self.y2+=x
        self.w1_2.config(text=f'{self.y2}')
    y3=0
    def bowler_function3(self,x):
        self.y3+=x
        self.w1_3.config(text=f'{self.y3}')
    y4=0
    def bowler_function4(self,x):
        self.y4+=x
        self.w1_4.config(text=f'{self.y4}')
    y5=0
    def bowler_function5(self,x):
        self.y5+=x
        self.w1_5.config(text=f'{self.y5}')
    y6=0
    def bowler_function6(self,x):
        self.y6+=x
        self.w1_6.config(text=f'{self.y6}')
    y7=0
    def bowler_function7(self,x):
        self.y7+=x
        self.w1_7.config(text=f'{self.y7}')
    y8=0
    def bowler_function8(self,x):
        self.y8+=x
        self.w1_8.config(text=f'{self.y8}')
    y9=0
    def bowler_function9(self,x):
        self.y9+=x
        self.w1_9.config(text=f'{self.y9}')
    y10=0
    def bowler_function10(self,x):
        self.y10+=x
        self.w1_10.config(text=f'{self.y10}')
    y11=0
    def bowler_function11(self,x):
        self.y11+=x
        self.w1_11.config(text=f'{self.y11}')
    
    
        
        
    
        
    
        
if __name__ == '__main__':
    pass
    #  MatchStart()
   