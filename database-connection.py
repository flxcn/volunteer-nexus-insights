import mysql.connector, matplotlib

print(matplotlib.__version__)

mydb = mysql.connector.connect(
  host = 'localhost',
  port = '8889',
  user = 'root',
  password = 'root',
  database = 'python_test'
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("SHOW databases")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)