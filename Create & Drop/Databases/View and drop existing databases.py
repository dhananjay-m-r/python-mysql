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

ViewDBList = input('Before dropping the database would you like to view the list of databases present on your server? (Y/N): ')
Yes = 'Yy'

if ViewDBList in Yes:
    c = 0
    databases = ("show databases")
    y.execute(databases)
    
    print('')
    print('»»——————---——————-««')
    print('The list of database present on your server is as below: ')
    for (databases) in y:
        print('-> ', databases[0])
        c += 1
    print('')
    print('Total no of database detected on your server is: ', c)

print('')
print('»»——————---——————-««')
print('')

m = input('Enter the database name which you would like to drop/delete: ')
n = 'drop database ' + m + ';'

print('')

try:
    y.execute(n)
    print('The database ', m, ' dropped successfully!')
except mysql.connector.Error:
    print('Error Encountered! Database doesnt exist!!')
    print('Program terminated!!')
finally:
    print('')
    print('Thank you for using the program')
    print('»»——————---——————-««')
    print('Source Code: Dhananjay M.R')

x.close()
