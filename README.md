# volunteer-nexus-insights
Breaking down the data from the VolunteerNexus platform

## Getting Started

In your terminal, first run these two commands:

```python3 -m pip install mysql-connector-python```

```python3 -m pip install matplotlib```

## Connecting to the Database
```
import mysql.connector

mydb = mysql.connector.connect(
  host = 'localhost',
  port = '8889',
  user = 'root',
  password = 'root',
  database = 'volunteer_nexus_data'
)
```