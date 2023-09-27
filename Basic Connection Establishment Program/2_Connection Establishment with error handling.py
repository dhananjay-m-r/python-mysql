import mysql.connector

try:
    x = mysql.connector.connect(host='locahost', user='root', password='admin.123')
except mysql.connector.Error:
    print('Sorry Check your Database Host User ID/Password!')

try:
    if x.is_connected():
        db_info = x.get_server_info()
        print('Connection to MySQL', db_info, 'established successfully!')
except NameError:
    print('Program Terminated')

finally:
    print('Thanks for using the program')
    print('»»——————---——————-««')
    print('Source Code by: Dhananjay M.R')
