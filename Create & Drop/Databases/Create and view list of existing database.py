m = input('Enter the database name which you would like to create: ')
n = 'create database ' + m + ';'

print('')
print('Kindly enter your database details below to create the database', m)
print('')

a = input('Enter your host ID: ')
b = input('Enter your MySQL User ID: ')
c = input('Enter the password for the mentioned MySQL User: ')

import mysql.connector
x = mysql.connector.connect(host = a, user = b, password = c)
y = x.cursor()
y.execute(n)

print('Database Successfully Created!')
print('')
print('»»——————---——————-««')

View = input('Would you like to view the list of all the databases present on your server? (Y/N): ')
print('')
Yes = 'Yy'

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

x.close()

print('')
print('Thank you for using the program')
print('»»——————---——————-««')
print('Source Code: Dhananjay M.R')
