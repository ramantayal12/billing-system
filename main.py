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


def main():
    print("Welcome to Billing System")
    option = 0
    while( option != 5 ):
        print("1 : Add New Customer ")
        print("2 : Show Data of Customer ")
        print("3 : Show Account Balance ")
        print("4 : Add Credit/Debit to Account ")
        print("5 : Exit the Application")
        print("Enter Option Number : ")
        option = int(input())
        if option == 5:
            break

if __name__ == "__main__":
    conn = sql_connection('cutomer-data.db')
    option1(conn)
