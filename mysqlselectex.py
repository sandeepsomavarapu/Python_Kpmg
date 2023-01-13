
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="kpmg")

mycursor=mydb.cursor()

mycursor.execute("select * from employees")
data =mycursor.fetchall()
 
for row in data:
        print("Employee Number:",row[0])
        print("Employee Name:",row[1])
        print("Employee Salary:",row[2])
        print("Employee Address:",row[3])

eid=128
mycursor.execute(f"SELECT * FROM employees where empid={eid}")

myresult = mycursor.fetchone()

print(myresult)
#for x in myresult:
#  print(x)