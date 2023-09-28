import mysql.connector

x = input('Enter your host ID: ')
y = input('Enter your MySQL User ID: ')
z = input('Enter the password for the mentioned MySQL User: ')

try:
    m = mysql.connector.connect(host=x, user=y, password=z)

except mysql.connector.Error:
    print('Sorry Check your Database Host User ID/Password!')

try:
    if m.is_connected():
        db_info = m.get_server_info()
        print('Connection to MySQL', db_info, 'established successfully!')
except AttributeError:
    print('Program Terminated')

finally:
    print('Thanks for using the program')
    print('»»——————---——————-««')
    print('Source Code by: Dhananjay M.R')
