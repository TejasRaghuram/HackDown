import mysql.connector
import sys

BOZO = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="BOZO",
    database="bozo"
)

cursor = BOZO.cursor()

id = 0
cursor.execute("SELECT * FROM questions")
result = cursor.fetchall()
for row in result:
    id += 1

sqlQF = "INSERT INTO questions (name, tag, question, id) VALUES (%s, %s, %s, %s)"
qInput = (sys.argv[1], sys.argv[2], sys.argv[3], id)
cursor.execute(sqlQF, qInput)
BOZO.commit()
