import tkinter as tk

import sqlite3
from sqlite3 import Error


def sql_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Database connected")
    except:
        print(Error)
    return conn


def option1(conn):
    cursor_obj = conn.cursor()
    name = str(input('Enter name of Customer :'))
    opn_bal = int(input('Enter Opening Balance of Customer :'))
    entities = (name,opn_bal)
    cursor_obj.execute('insert into basic_data(Name,Balance) values(?,?)',entities)
    print('Customer Added to the Database File ')
    conn.commit()


def option2(conn):
    cursor_obj = conn.cursor()
    cursor_obj.execute('SELECT Name,Balance FROM basic_data')
    data = cursor_obj.fetchall()
    print('Customer Name    Account Balance')
    for row in data:
        print(row)


def option3(conn2):
    cursor_obj = conn2.cursor()
    cursor_obj.execute('SELECT * FROM Balance')
    data = cursor_obj.fetchall()
    print('Account Balance is : ')
    for row in data:
        print(row)


def option4(conn2,cre = 0,deb = 0):
    cursor_obj = conn2.cursor()
    cre = int(input('Enter Credit to be Added : '))
    deb = int(input('Enter Debit to be Added : '))
    cursor_obj.execute('SELECT * FROM Balance LIMIT 1')
    last_balance_l = cursor_obj.fetchall()
    last_balance = last_balance_l[0]
    last_balance = last_balance[0]
    last_balance += cre
    last_balance -= deb
    query = 'UPDATE Balance SET Account_Balance = ' + str(last_balance)
    cursor_obj.execute(query)
    conn2.commit()

def option5(conn,name,amnt):
    cursor_obj = conn.cursor()
    query1 = 'SELECT * FROM basic_data WHERE Name = '+ name
    cursor_obj.execute(query1)
    last_balance_l = cursor_obj.fetchall()
    last_balance = last_balance_l[1]
    last_balance = last_balance[1]
    last_balance -= amnt
    query2 = ' UPDATE FROM basic_data SET Balance =' + str(last_balance)+' WHERE Name = '+ name
    cursor_obj.execute(query2)
    cursor_obj.commit()

def main():
    conn = sql_connection('customer-data.db')
    conn2 = sql_connection('my_sheet.db')
    top = tk.Tk()
    top.title(' Billing System ')

    ## Implementing Buttons 
    button1 = tk.Button(top,text = "1. Add New Customer ",width = 25,command = option1(conn))
    button1.pack()

    button2 = tk.Button(top,text = "2 : Show Data of Customer ",width = 25,command = option2(conn))
    button2.pack()

    button3 = tk.Button(top,text = "3 : Show Account Balance ",width = 25,command = option3(conn2))
    button3.pack()

    button4 = tk.Button(top,text = "4 : Add Credit/Debit to Account ",width = 25,command = option4(conn2))
    button4.pack()

    button5 = tk.Button(top,text = "5 : Generate New Sale Bill : ",width = 25,command = top.destroy)
    button5.pack()

    button6 = tk.Button(top,text = "6 : Enter New Purchase Bill : ",width = 25,command = top.destroy)
    button6.pack()

    button7 = tk.Button(top,text = "7 : Exit the Application",width = 25,command = top.destroy)
    button7.pack()


    top.mainloop()

if __name__ == "__main__":
    main()