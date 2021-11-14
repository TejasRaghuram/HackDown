import mysql.connector
import sys

BOZO = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="BOZO",
    database="bozo"
)

cursor = BOZO.cursor()

sqlAF = "INSERT INTO answers (name, answer, id) VALUES (%s, %s, %s)"
aInput = (sys.argv[1], sys.argv[2], int(sys.argv[3]))
cursor.execute(sqlAF, aInput)
BOZO.commit()
