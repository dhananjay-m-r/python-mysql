import mysql.connector as a
x = a.connect(host='localhost', user='root', password='admin.123')
if x.is_connected():
    db_info = x.get_server_info()
    print('Connection to MySQL', db_info, 'established!')
