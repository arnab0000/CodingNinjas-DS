import sqlite3 as sql
db = sql.connect("University.sqlite")
cur = db.cursor()
# sql_query = 'create table Student(rollno int Primary key, Name Text, Age int)'
# cur.execute(sql_query)
# cur.execute('insert into Student values(101, "Arnab", 24)')
# db.commit()
# cur.execute('insert into Student values(102, "Jyoti", 34)')
# db.commit()
# name = "Somnath"
# rollno = 103
# age = 57
# cur.execute('insert into Student values(?, ?, ?)', (rollno, name, age))
# db.commit()
vals = [(104, "Mahua", 47), (105, "Ranveer", 26), (106, "Praveen", 22)]
cur.executemany('insert into Student values(?, ?, ?)', vals)
db.commit()