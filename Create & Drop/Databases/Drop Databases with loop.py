print('Before we get started, Kindly enter your database details below: ')
print('')

a = input('Enter your host ID: ')
b = input('Enter your MySQL User ID: ')
c = input('Enter the password for the mentioned MySQL User: ')

import mysql.connector
x = mysql.connector.connect(host = a, user = b, password = c)
y = x.cursor()

print('')
print('»»——————---——————-««')
print('')

c = 0
databases = ("show databases")
y.execute(databases)

print('')
print('»»——————---——————-««')
print('')
print('Here below is the list of database present on your server: ')
print('')

for (databases) in y:
    print('-> ', databases[0])
    c += 1

print('')
print('Total no of database detected on your server is: ', c)

print('')
print('»»——————---——————-««')
print('')

print('Dropping a database means you will loose the data stored in it as well')

def DropDatabase():
    m = input('Enter the database name which you would like to drop/delete: ')
    n = 'drop database ' + m + ';'

    print('')

    try:
        y.execute(n)
        print('The database ', m, ' dropped successfully!')
        print('')
        
        ShowRemaining = input('Do you want to view the updated list of databases on your server (Y/N): ')

        d = 0
        No = 'Nn'
        if ShowRemaining in Yes:
            databases = ("show databases")
            y.execute(databases)

            print('')
            print('»»——————---——————-««')
            print('')
            print('Here below is the updated list of database present on your server: ')
            print('')

            for (databases) in y:
                print('-> ', databases[0])
                d += 1
            print('')
            print('Currently you have', d, 'databases on your server')

            print('')
            print('»»——————---——————-««')
            print('')
        elif ShowRemaining not in No:
            print('Invalid Input! Skipping the function!')
            print('')
        
    except mysql.connector.Error:
        print('Error Encountered! Database doesnt exist!!')
        print('Enter a database name that exists!!')

print('')

confirmation = input('Would you like to terminate the program (Y/N): ')
Yes = 'Yy'
No = 'Nn'

while confirmation in No:
    LoopAgain = input('Do you want to drop more databases?(Y/N): ')
    print('')
    if LoopAgain in Yes:
        DropDatabase()
    elif LoopAgain not in No:
        print('Invalid Input! Kindly enter a valid Input')
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
