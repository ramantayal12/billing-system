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


def option3(conn2):
    cursor_obj = conn2.cursor()
    cursor_obj.execute('SELECT * FROM BALANCE')
    data = cursor_obj.fetchall()
    print('Account Balance is : ')
    for row in data:
        print(row)


def option5(conn):
    cursor_obj = conn.cursor()
    cursor_obj.execute('SELECT Name,Balance FROM basic_data')
    data = cursor_obj.fetchall()
    print('Customer Name    Account Balance')
    for row in data:
        print(row)
    

def main():
    print("Welcome to Billing System")
    conn = sql_connection('customer-data.db')
    conn2 = sql_connection('my_sheet.db')
    option = 0
    while( option != 6 ):
        print("1 : Add New Customer ")
        print("2 : Show Data of Customer ")
        print("3 : Show Account Balance ")
        print("4 : Add Credit/Debit to Account ")
        print("5 : Show All Customers ")
        print("6 : Exit the Application")
        print("Enter Option Number : ")
        option = int(input())
        if option == 1:
            option1(conn)
            continue
        elif option == 3:
            option3(conn2)
            continue
        elif option == 5:
            option5(conn)
            continue
        elif option == 6:
            print(' Thank you ')
            break


if __name__ == "__main__":
    main()
