import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="student")

mycursor = mydb.cursor()

sql = "INSERT INTO details (name, age,course,place) VALUES ('Jasir',23,'MCA','MLP')"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record inserted.")