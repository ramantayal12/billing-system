import sqlite3


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
    main()