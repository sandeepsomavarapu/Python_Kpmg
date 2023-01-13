
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="kpmg")

mycursor=mydb.cursor()

mycursor.execute("delete from employees where empid=124");

mydb.commit();