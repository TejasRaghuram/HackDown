import mysql.connector
import sys

BOZO = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="BOZO",
    database="bozo"
)

cursor = BOZO.cursor()

cursor.execute("SELECT "+sys.argv[1]+" FROM questions WHERE id = "+sys.argv[2])
result = cursor.fetchone()

print(result)
