import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# Establish database connection
mydb = mysql.connector.connect(
  host = 'localhost',
  port = '8889',
  user = 'root',
  password = 'root',
  database = 'volunteer_nexus_data'
)

# Run query
mycursor = mydb.cursor()

sql = "SELECT time_submitted FROM engagements" 

mycursor.execute(sql)

myresult = mycursor.fetchall()

# Process results
times = list(map(lambda x: x[0], myresult))

x = np.array(times)

# Plot histogram graph
plt.hist(x)

# Assign labels
plt.xlabel("Time")
plt.ylabel("Frequency of Engagements")

# Show histogram graph
plt.show()