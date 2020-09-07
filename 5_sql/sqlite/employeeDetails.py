import sqlite3 as sql
db = sql.connect("Employee_Details.sqlite")
cur = db.cursor()
# sql_query = 'create table Employee(employee_id int Primary key, name Text, Age int, department Text, salary int)'
# cur.execute(sql_query)
# employee_id=[101,102,103,104,105,106,107,108,109,110,111,112,113]
# name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
# age=[25,27,25,24,30,26,23,26,25,26,29,24]
# department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
# salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]
# print(len(employee_id), len(name), len(age), len(department), len(salary))
# for i in range(len(name)):
#     cur.execute('insert into Employee values(?, ?, ?, ?, ?)', (employee_id[i], name[i], age[i], department[i], salary[i]))
# db.commit()
# print("Done")
cur.execute('select department, count(*) from Employee group by department')
ans = cur.fetchall()
for i in ans:
    print(i[0], i[1])