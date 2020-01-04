from django.db import models

import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Xhc654477358",
        database="mysql_test"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM mysql_test1")

    myresult = mycursor.fetchall()
    print(myresult)
except Exception as e:
    print(e)
