import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='88328832'
)

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("db set")