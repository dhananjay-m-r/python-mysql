Yes = 'Yy'
No = 'Nn'

def InitiateProgram():
    print('Program now available at GitHub \n')
    print('Visit github.com/dhananjay-m-r/python-mysql for other programs\n')
    print('»»——————---——————-«« \n')
    input('Press any key to start the program...\n')
    print('»»——————---——————-«« \n')
    ModuleCheck()

def ModuleCheck():
    try:
        print('Checking for required module! \n\nModule check complete! \n')
        import mysql.connector as MySQL
        global MySQL
        print('The required module to establish session with MySQL has been found! \n')
        SessionEstablishConfirmation()

    except ImportError:
        print('Sorry! The required module to establish session with MySQL not found! \n')
        print('»»——————---——————-«« \n')
        print('Kindly install the required module! \n')
        Terminate()

def SessionEstablishConfirmation():
    Choice = input('Would you like to log in to your MySQL server (Y/N): ')

    if Choice in Yes or Choice.lower() == 'yes':
        SessionEstablishment()
    elif Choice in No or Choice.lower() == 'no':
        Terminate()
    else:
        print('\nInvalid Input')
        Terminate()

def SessionEstablishment():
    print('\nKindly Enter your MySQL server sign in credentials \n')
    HostID = input('Enter your MySQL server HostID: ')
    User = input(f'Enter your MySQL server User ID to sign in to {HostID}: ')
    Password = input(f'Enter your password for the user {User} : ')

    try:
        global x
        global y
        
        x = MySQL.connect(host = HostID, user = User, password = Password)
        y = x.cursor()
        
        db_info = x.get_server_info()
        print('\nConnection to MySQL', db_info, 'established successfully!')
        
        Menu()

    except MySQL.Error:
        print('\nAuthentication failed!\nIncorrect User ID/Password/HostID! Kindly Enter valid credentials! \n')
        Choice = input('Would you like to enter your MySQL server credentials again? (Y/N):')

        if Choice in Yes or Choice.lower() == 'yes':
            SessionEstablishment()

        elif Choice in No or Choice.lower() == 'no':
            Terminate()

        else:
            print('Invalid input! Terminating Programming!')
            Terminate()

def ViewDatabaseList():
    
    y = x.cursor()
    databases = ('Show databases;')
    y.execute(databases)

    c = 0

    for (databases) in y:
        print('-> ', databases[0])
        c += 1

    print('\nThe total number of databases detected on your server is: ', c)

    Menu()

def CreateDatabase():
    NewdbName = input('Enter the new database name which you would like to create: ')
    command = 'create database ' + NewdbName + ';'

    try:
        y = x.cursor()
        y.execute(command)

        print(f'\nDatabase {NewdbName} created successfully!\n')
        Choice = input('Would you like to view the updated list of database? (Y/N): ')
        if Choice in Yes or Choice.lower() == 'yes':
            ViewDatabaseList()
        elif Choice in No or Choice.lower() == 'no':
            Menu()
        else:
            print('\n Invalid Input!\nReturning to Main Menu')
            Menu()

    except MySQL.Error:
        print(f'\nCould not create the database {NewdbName}! Kindly check if database {NewdbName} already exists\n')
        Choice = input('Would you like to view the updated list of database? (Y/N): ')

        if Choice in Yes or Choice.lower() == 'yes':
            ViewDatabaseList()

        elif Choice in No or Choice.lower() == 'no':
            Menu()

        else:
            print('\n Invalid Input!\nReturning to Main Menu')
            Menu()
            
def DropDatabase():
    print('Disclaimer: Dropping a database means that you will loose the data stored in it as well! \n')
    Choice1 = input('Are you sure that you want drop databases (Y/N): ')

    if Choice1 in Yes or Choice1.lower() == 'yes':

        Choice2 = input('\nBefore dropping the database would like to view the list of existing database on your server? (Y/N): ')

        if Choice2 in Yes or Choice2.lower() == 'yes':
            y = x.cursor()
            databases = ('Show databases;')
            y.execute(databases)

            c = 0
            print('')

            for (databases) in y:
                print('-> ', databases[0])
                c += 1
                
            print('\nThe total number of databases detected on your server is: ', c)

        elif Choice2 in No or Choice2.lower() == 'no':
            print('')

        else:
            print('\nInvalid Input!\nReturning to Main Menu')
            Menu()

        dbDrop = input('Enter the database name which you would like to drop: ')
        command = 'drop database ' + dbDrop + ';'

        try:
            y = x.cursor()
            y.execute(command)

            print('\nDatabase dropped!\n')
            Choice3 = input('Would you like to view the updated list of database? (Y/N): ')
        
            if Choice3 in Yes or Choice3.lower() == 'yes':
                ViewDatabaseList()
            elif Choice3 in No or Choice3.lower() == 'no':
                Menu()
            else:
                print('\n Invalid Input!\nReturning to Main Menu')
                Menu()

        except MySQL.Error:
            print(f'\nCould not delete the database {dbDrop}! Kindly check if database {dbDrop} exists\n')
            Choice4 = input('Would you like to view the updated list of database? (Y/N): ')

            if Choice4 in Yes or Choice4.lower() == 'yes':
                ViewDatabaseList()

            elif Choice4 in No or Choice4.lower() == 'no':
                Menu()
    
            else:
                print('\nInvalid Input!\nReturning to Main Menu')
            Menu()
        
    elif Choice1 in No or Choice1.lower() == 'no':
        Menu()
        
    else:
        print('\nInvalid Input!\nReturning to Main Menu')
        Menu()
    
    dbDrop
    
def Menu():
    input('\nPress any key to continue to the main menu...')
    print('\n»»——————- Main Menu -——————-«« \n')
    print('Press 1 to view the list of existing databases \nPress 2 to create a database \nPress 3 to drop a database')
    print('Press 4 to terminate the program \n')
    option = int(input('Enter your choice here: '))
    print('')

    if option == 1:
        ViewDatabaseList()
    elif option == 2:
        CreateDatabase()
    elif option == 3:
        DropDatabase()
    elif option == 4:
        x.close()
        Terminate()
    else:
        print('\nInvalid Input! \nKindly enter a valid choice!')
        Menu()

def Terminate():
    print('\nProgram Terminated! \n \nThanks for using the program!')
    print('»»——————---——————-««')
    print('Source Code by: Dhananjay M.R \n')
    input('Press any key to exit...')
    exit()

InitiateProgram()
