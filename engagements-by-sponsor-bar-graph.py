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
sql = "SELECT sponsors.sponsor_name, SUM(contribution_value) FROM engagements INNER JOIN sponsors ON engagements.sponsor_id = sponsors.sponsor_id GROUP BY engagements.sponsor_id ASC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

# Process results
sponsors = list(map(lambda x: x[0], myresult))
contribution_totals = list(map(lambda x: x[1], myresult))

x = np.array(sponsors)
y = np.array(contribution_totals)

# Plot bar graph
plt.barh(x,y)

# Assign labels
plt.xlabel("Total Contribution Value")
plt.ylabel("Sponsor Name")

# Show bar graph
plt.show()