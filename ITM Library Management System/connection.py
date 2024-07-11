import sqlite3
#create database connection


conn = sqlite3.connect('itmlibrary.db')
cur=conn.cursor()
# cur.execute('''
#             CREATE TABLE add_book(
#                 book_id TEXT PRIMARY KEY,
#                 book_name TEXT NOT NULL,
#                 author TEXT NOT NULL,
#                 publisher TEXT not NULL,
#                 edition text NOT NULL,
#                 category TEXT NOT NULL,
#                 book_description TEXT NOT NULL,
#                 quantity INTEGER NOT NULL,
#                 shelf_location TEXT NOT NULL,
#                 price REAL NOT NULL,
#                 book_image BLOB NOT NULL
                
                
#             )
#             ''')


# cur.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS add_student(
#         student_id TEXT PRIMARY KEY,
#         library_id TEXT NOT NULL UNIQUE,
#         student_name TEXT NOT NULL,
#         student_email TEXT NOT NULL,
#         student_phone TEXT NOT NULL,
#         student_department TEXT NOT NULL,
#         student_course TEXT NOT NULL,
#         student_year TEXT NOT NULL,
#         student_address TEXT NOT NULL,
#         student_gender TEXT NOT NULL,
#         student_image BLOB
#     )
#     '''
# )
# cur.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS issue_book(
#         book_id TEXT  NOT NULL,
#         book_name TEXT NOT NULL,
#         book_auther TEXT NOT NULL,
#         publisher TEXT NOT NULL,
#         edition TEXT NOT NULL,
#         student_id TEXT  not null,
#         library_id TEXT  not null,
#         student_name TEXT NOT NULL,
#         issue_date TEXT NOT NULL,
#         return_date TEXT NOT NULL,
#         issue_type TEXT NOT NULL  
#     )
    
#         '''
# )
# cur.execute(
#     '''
#     create table return_book(
#         book_id text Not null,
#         student_id text NOT NULL,
#         library_id text NOT NULL,
#         return_date TEXT NOT NULL,
#         due_date TEXT NOT NULL,
#         fine REAL NOT NULL
        
#     )
#     '''

# )

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS payment_history (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL ,
        library_id TEXT NOT NULL ,
        student_name TEXT NOT NULL,
        book_id TEXT NOT NULL ,
        book_name TEXT NOT NULL,
        payment_date TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_type TEXT NOT NULL
    )
    '''
)
# cur.execute(
#     '''
#     CREATE TABLE user(
#         admin_name TEXT NOT NULL,
#         username TEXT primary key,
#         password TEXT NOT NULL,
#         email TEXT NOT NULL,
#         phone TEXT NOT NULL
       
#     )
#     '''
# )
# cur.execute('drop table payment_history')

conn.commit()

#close database connection
        