from random import choices
from re import M
import mysql.connector
# from mysql.connector import cursor
# from mysql.connector.cursor_cext import CMySQLCursorNamedTuple

import time


connec=mysql.connector.connect(user="root"
,password=""
,host="localhost",
database="banksytem")
id=int(input("Enter Id:"))











def menu():
        print("1.Add Money:")
        print("2.Check Balance:")
        print("3.Withdrawal Money")


        choices=int(input("Enter the Number:"))
        if(choices==1):
            Money=int(input("How Much Money to add:"))
            Money1=Money+row[1]
            update="UPDATE bank set Money={} WHERE PinCode={}".format(Money1,id)
            con=mysql.connector.connect(host="localhost",user="root",password="",database="banksytem")
            cam=con.cursor()

            cam.execute(update)
            con.commit()
            print("Money Added Rs.",Money)
            exit()
        elif choices==2:
            print("Balance is",row[1])
        elif choices==3:
            Wid=int(input("How Much Money to withdrawal:"))
            Money1=row[1]-Wid
            if(Money1<=0):
                print("No Money")
                exit()
            update="UPDATE bank set Money={} WHERE PinCode={}".format(Money1,id)
            con=mysql.connector.connect(host="localhost",user="root",password="",database="banksytem")
            cam=con.cursor()
            cam.execute(update)
            con.commit()        
        else:
            print("Invaild ID")    
    


query="SELECT * FROM bank"
cur=connec.cursor()
cur.execute(query)
for row in cur:
    if(id==row[0]):
        print("Bank System Got it Name is",row[3])
        menu()
    else:
        exit()


