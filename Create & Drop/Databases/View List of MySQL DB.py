print('Before we get started, Kindly enter your database details below: ')
print('')

HostID = input('Enter your host ID: ')
UserID = input('Enter your MySQL User ID: ')
MySQLPassword = input('Enter the password for the mentioned MySQL User: ')

print('')
print('»»——————---——————-««')
print('')
start = input('Press any key to start the program! ')

import mysql.connector
x = mysql.connector.connect(host = HostID, user = UserID, password = MySQLPassword)
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

print('Function Completed')
print('')
print('Program Terminated!')

print('')
x.close()
print('MySQL Python Connection Closed!')

print('')
print('Thank you for using the program')
print('')
print('»»——————---——————-««')
print('Source Code by: Dhananjay M.R')
