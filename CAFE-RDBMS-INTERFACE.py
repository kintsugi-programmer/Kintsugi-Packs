#Wednesday, January 27, 2021
#ANTEIKU_CAFE COUNTER INTERFACE PROGRAM SOURCE CODE
#ANTEIKU_CAFE COUNTER INTERFACE PROGRAM SOURCE CODE

#MODULES USED IN THE PROGRAM

import mysql.connector

import datetime

import csv

#CONNECTION ESTABLISHMENT 

mycon=mysql.connector.connect(host="localhost",user="root",passwd="IIT-JEE",database="anteiku_cafe")

if mycon.is_connected():

        print("WELCOME TO ANTEIKU_CAFE COUNTER INTERFACE PROGRAM !!!!")

cursor=mycon.cursor()

#OTHER FUNCTIONS

def commit():

        print("\n")

        print("DATA EXECUTED SUCCESSFULLY !!!!")

        mycon.commit()

        print("\n")

def historia():

        a=str(input("ENTER YOUR NAME :"))

        noww=str(datetime.datetime.now())

        noww=noww.split(" ")

        b=str(noww[-2])

        c=str(noww[-1])

        st="insert into history(NAME,DATE,TIME) values('{}','{}','{}')".format(a,b,c)

        cursor.execute(st)

        mycon.commit()

#ENTER NEW CUSTOMER ORDER

def one():

        fields=["ID","NAME","DATE","TIME","PHONE_NO","ITEMS","AMOUNT","PAYMENT_MODE","ORDER_STATUS"]

        a=input("ENTER ID :")

        b=input("ENTER NAME :")

        noww=str(datetime.datetime.now())

        noww=noww.split(" ")

        c=str(noww[-2])

        d=str(noww[-1])

        e=input("ENTER PHONE NO. :")

        f=str(input("ENTER ITEMS :"))

        cal=input("DO YOU WANT TO USE CALCULATOR (y/n):")

        if cal=="y":

                eight()

        i=input("ENTER NET AMOUNT :")

        j=input("ENTER PAYMENT MODE :")

        k="PENDING"

        st="insert into customer values({},'{}','{}','{}',{},'{}',{},'{}','{}')".format(a,b,c,d,e,f,i,j,k)

        cursor.execute(st)

        commit()

#COMPLETE ORDER

def two():

        a="COMPLETED"

        b=int(input("ENTER ID OF CUSTOMER ORDER LIST :"))

        st="update customer set ORDER_STATUS='{}' where ID={}".format(a,b)

        cursor.execute(st)

        commit()

#CANCEL ORDER

def three():

        a="CANCELLED"

        b=int(input("ENTER ID OF CUSTOMER ORDER LIST :"))

        st="update customer set ORDER_STATUS='{}' where ID={}".format(a,b)

        cursor.execute(st)

        commit()

#SHOW MENU

def four():

        st="select * from menu"

        cursor.execute(st)

        data=cursor.fetchall()

        print("[ ID,ITEM_NAME,CATEGORY,TYPE,RATE ]")

        for i in data:

                for j in i:

                        print(j,end=" , ")

                print()

        commit()        

#SHOW CUSTOMER DETAILS

def five():

        st="select * from customer"

        cursor.execute(st)

        data=cursor.fetchall()

        print("[ ID,NAME,DATE,TIME,PHONE_NO,ITEMS,AMOUNT,PAYMENT_MODE,ORDER_STATUS ]")

        for i in data:

                for j in i:

                        print(j,end=" , ")

                print()

        commit()        

#SHOW STAFF DETAILS

def six():

        st="select * from staff"

        cursor.execute(st)

        data=cursor.fetchall()

        print("[ ID,NAME,DESIGNATION,PHONE_NO ]")

        for i in data:

                for j in i:

                        print(j,end=" , ")

                print()

        commit()        

#SHOW USER ACCESS HISTORY

def seven():

        st="select * from history"

        cursor.execute(st)

        data=cursor.fetchall()

        print("[ NAME,DATE,TIME ]")

        for i in data:

                for j in i:

                        print(j,end=" , ")

                print()

        commit()        

#OPEN CALCULATOR

def add(x, y):

        return x + y

def subtract(x, y):

        return x - y

def multiply(x, y):

        return x * y

def divide(x, y):

        return x / y

def eight():

        print("Select operation.")

        print("1.Add")

        print("2.Subtract")

        print("3.Multiply")

        print("4.Divide")

        while True:

                choice = input("Enter choice(1/2/3/4): ")

                if choice in ('1', '2', '3', '4'):

                        num1 = float(input("Enter first number: "))

                        num2 = float(input("Enter second number: "))

                        if choice == '1':

                                print(num1, "+", num2, "=", add(num1, num2))

                        elif choice == '2':

                                print(num1, "-", num2, "=", subtract(num1, num2))

                        elif choice == '3':

                                print(num1, "*", num2, "=", multiply(num1, num2))

                        elif choice == '4':

                                print(num1, "/", num2, "=", divide(num1, num2))

                        break

                else:

                        print("Invalid Input")

#CONVERT CUSTOMER LIST INTO EXCEL FILE

def nine():

        filename=str(input("FILE NAME :"))

        filename+=".csv"

        f=open(filename,'w',newline='')

        fields=["ID","NAME","DATE","TIME","PHONE_NO","ITEMS","AMOUNT","PAYMENT_MODE","ORDER_STATUS"]

        csv.writer(f).writerow(fields)

        cursor.execute("select * from customers ")

        data=cursor.fetchall()

        list1=[]

        for k in data:

                a=[]

                for j in k:

                        a.append(j)

                list1.append(a)

        csv.writer(f).writerows(list1)

        f.close()

        commit()

#SHOW AMOUNT COLLECTED TODAY

def ten():

        noww=str(datetime.datetime.now())

        noww=noww.split(" ")

        a=str(noww[-2])

        st="select SUM(AMOUNT) from customer where date='{}'".format(a)

        cursor.execute(st)

        data=cursor.fetchall()

        print("[ AMOUNT COLLECTED TODAY]")

        print(data)

        commit()

#CONVERT HISTORY LIST INTO EXCEL FILE

def eleven():

        filename=str(input("FILE NAME :"))

        filename+=".csv"

        f=open(filename,'w',newline='')

        fields=["NAME","DATE","TIME"]

        csv.writer(f).writerow(fields)

        cursor.execute("select * from history ")

        data=cursor.fetchall()

        list1=[]

        for k in data:

                a=[]

                for j in k:

                        a.append(j)

                list1.append(a)

        csv.writer(f).writerows(list1)

        f.close()

        commit()

#CLOSE PROGRAM

def closeproj(): 
        mycon.close()
        if not mycon.is_connected():

                print("THANK YOU FOR USING THIS PROGRAM !!!!")

#MENU

historia()

setup='on'

while setup=='on':

        print("QUERIES\t:\n\t1.ENTER NEW CUSTOMER ORDER\n\t2.COMPLETE ORDER\n\t3.CANCEL ORDER\n\t4.SHOW MENU\n\t5.SHOW CUSTOMER DETAILS\n\t6.SHOW STAFF DETAILS\n\t7.SHOW USER ACCESS HISTORY\n\t8.OPEN CALCULATOR\n\t9.CONVERT CUSTOMER LIST INTO EXCEL FILE\n\t10.SHOW AMOUNT COLLECTED TODAY\n\t11.CONVERT USER ACCESS HISTORY LIST INTO EXCEL FILE\n\t12.CLOSE PROGRAM\n\tNOTE\t:\tTO RUN ANY QUERY ,ENTER IT\'S SERIAL NUMBER AT RUN\n ")

        run=int(input("\tRUN\t:\t"))

        if run==1:

                one()

        elif run==2:

                two()

        elif run==3:

                three()

        elif run==4:

                four()

        elif run==5:

                five()

        elif run==6:

                six()

        elif run==7:

                seven()

        elif run==8:

                eight()

        elif run==9:

                nine()

        elif run==10:

                ten()

        elif run==11:

                eleven()

        elif run==12:

                closeproj()

                setup="off"

        else :

                print("ERROR !!!!\nTYPE CORRECTLY")