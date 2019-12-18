from sqlalchemy import create_engine
import pandas as pd
import requests
import time
import os

# Request json
data = {
    "start_date": "2019-01-01",
    "end_date": "2019-09-07",
    "columns": [
        "spend",
        "revenue",
        "profit",
        "margin",
        "nb_impressions",
        "ecpm"
    ]
}

# Send the json request to the API via a Post method
response = requests.post(
    "https://data-analyst-test.madboxgames.io/api/public/profit/get",
    json=data,
)
data = dict(response.json())['data']['data']

# Put the response into a Dataframe
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df = df.reset_index()\
    .drop(['index'], axis='columns')\
    .set_index(['date'])
print(df)

# Retry until the database service is ready to be accessed
for i in range(20):
    try:
        # Establish the Database connection
        database = os.environ['MY_SQL_IP']
        db_connection_str = f"mysql+pymysql://root:123@{database}:3306/madbox"
        db_connection = create_engine(db_connection_str)

        # insert the data in the database
        df.to_sql("madbox_api", db_connection)
        print('succeed in inserting data into database')
        break
    except Exception as e:
        print('failed connection to database')
        print(db_connection_str)
        print(e)
        # Wait for the Database to start before insert data into it
        time.sleep(5)
