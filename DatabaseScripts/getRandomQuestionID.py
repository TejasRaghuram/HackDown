import mysql.connector
import random

BOZO = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="BOZO",
    database="bozo"
)

cursor = BOZO.cursor()

length = 0
cursor.execute("SELECT id FROM questions")
result = cursor.fetchall()
id = random.choice(result)

print(id)
