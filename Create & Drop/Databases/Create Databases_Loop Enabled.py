print('Before we get started, Kindly enter your database details below: ')
print('')

a = input('Enter your host ID: ')
b = input('Enter your MySQL User ID: ')
c = input('Enter the password for the mentioned MySQL User: ')

import mysql.connector
x = mysql.connector.connect(host = a, user = b, password = c)
y = x.cursor()

Yes = 'Yy'

print('')

Precheck = input('Before adding a database, would you like to take a look in the existing database list on the server? (Y/N): ')

if Precheck in Yes:
    c = 0

    y = x.cursor()
    databases = ("show databases")
    y.execute(databases)

    print('»»——————---——————-««')
    print('The list of database present on your server is as below: ')
    
    for (databases) in y:
        print('-> ', databases[0])
        c += 1
    
    print('')
    print('Total no of database detected on your server is: ', c)

def CreateDatabase():
    m = input('Enter the database name which you would like to create: ')
    n = 'create database ' + m + ';'
    
    y = x.cursor()
    y.execute(n)

    print('')
    print('Database Successfully Created!')
    print('')
    print('»»——————---——————-««')

    print('')
    View = input('Would you like to view the list of all the databases present on your server? (Y/N): ')
    print('')

    No = 'Nn'

    if View in Yes:
        c = 0
        y = x.cursor()

        databases = ("show databases")
        y.execute(databases)
        print('»»——————---——————-««')
        print('The list of database present on your server is as below: ')
        
        for (databases) in y:
            print('-> ', databases[0])
            c += 1
        print('')
        print('Total no of database detected on your server is: ', c)

        print('')
        print('»»——————---——————-««')
    
    elif View in No:
        print('')
    
    else:
        print('Invalid Input! Skipping to function')
print('')

confirmation = input('Would you like to terminate the program (Y/N): ')
No = 'Nn'

while confirmation in No:
    LoopAgain = input('Do you want to add more databases?(Y/N): ')
    print('')
    if LoopAgain in Yes:
        CreateDatabase()
    elif LoopAgain not in No:
        print('Invalid Input! Kindly enter a valid input!')
    else:
        break

print('Program Terminated!')

print('')
x.close()
print('MySQL Python Connection Closed!')

print('')
print('Thank you for using the program')
print('»»——————---——————-««')
print('Source Code by: Dhananjay M.R')
