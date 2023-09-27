import mysql.connector
try:
    x = mysql.connector.connect(host='localhost', user='root', password='admin.123')
except mysql.connector.Error:
    print('Sorry Check your Database Host User ID/Password!')
if x.is_connected():
    db_info = x.get_server_info()
    print('Connection to MySQL', db_info, 'established successfully!')
