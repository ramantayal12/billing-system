//
//  main.cpp
//  Customer_Data
//
//  Created by Tayal on 30/04/20.
//  Copyright © 2020 tayal. All rights reserved.
//

#include<iostream>
#include<stdio.h>
#include<fstream>
#include<string>


using namespace std;
fstream myfile;


class account_balance{
  
    int balance = 0;
public:
    void add_credit( int amnt ){
        this->balance += amnt;
    }
    void add_debit( int amnt ){
        this->balance -= amnt;
    }
    void show_balance(){
        cout<<"Account Balance is : ";
        cout<<this->balance<<endl;
    }
    
};



class customer_data{
    
    string name;
    int id;
    int debit = 0, credit = 0;
    int balance = 0;
public:
    void entry(int id,string name){
        this->name = name;
        this->id = id;
        this->balance = 0;
    }
    void update_credit( int credit ){
        this->credit = credit;
        this->balance += credit;
    }
    void update_dedit( int debit ){
        this->debit = debit;
        this->balance -= debit;
    }
    void show_cutomer(){
        cout<<"Customer ID : "<<this->id<<endl;
        cout<<"Customer Name : "<<this->name<<endl;
        cout<<"Customer Account Balance : "<<this->balance<<endl;
    }
    
};



int main(int argc, const char * argv[]) {
    
    
    cout<<"Welcome to Accounting "<<endl;
    int option = 0;
    
    
    
    myfile.open("data");
    
    
    while( option != 5 ){
        
        
        cout<<"1 : Add New Customer "<<endl;
        cout<<"2 : Show Data of Customer "<<endl;
        cout<<"3 : Show Account Balance "<<endl;
        cout<<"4 : Add Credit/Debit to Account "<<endl;
        cout<<"5 : Exit the Application"<<endl;
        cout<<"Enter Option Number : ";
        cin>>option;
        
        
        if( option == 1 ){
            
            string name;
            cout<<"Enter Name of Customer : ";
            cin>>name;
            myfile<<name<<endl;
            
        }
        
    }
    
    myfile.close();
    
    return 0;
}

