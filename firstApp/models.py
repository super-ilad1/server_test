from django.db import models
# -*- coding: utf-8 -*-
import mysql.connector



class doMysql():
    def __init__(self):

        self.mydb = mysql.connector.connect(
            host="101.133.134.177",
            user="window",
            passwd="Xhc654477358",
            database="mysql_test",
            port="3306"
        )

        self.mycursor = self.mydb.cursor()
        print('start to connect')

    def DoMysql(self, program, val=None, list=False, Many=False, lastrowid=False):
        '''program代表的是mysql语句，val代表的是增删查改的参数，list代表的是
                         select返回的对象全部变成列表形式而不是包裹着元组的那种形式
                         Many代表的是插入多个'''

        if program[0:6] == 'select':
            self.mycursor.execute(program)

            myresult = self.mycursor.fetchall()

            if list == True:
                myresult = [n for i in myresult for n in i]

            return myresult
        elif Many == True:

            self.mycursor.executemany(program, val)
            self.mydb.commit()
        else:
            self.mycursor.execute(program, val)
            self.mydb.commit()
            if lastrowid:
                return self.mycursor.lastrowid


if __name__ == '__main__':
    pass
    # a = doMysql()
    # # print(a.DoMysql('select * from mysql_test1'))
    # name='test'
    # age='23'
    # a.DoMysql('insert into mysql_test1 (name,age) values (%s,%s)', (name, age))

