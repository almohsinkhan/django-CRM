import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mohsin@2004'
)

# create a database object 
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute('CREATE DATABASE elederco')
print("ALL done!")

