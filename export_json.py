import json
import psycopg2

username = 'angelina'
password = 'angelina15'
database = 'Data Science Job Salaries'
host = 'localhost'
port = '1111'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:

    cur = conn.cursor()

    for table in ('jobs', 'experiencelevels', 'companieslocation', 'salaries'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

    for row in cur:
        rows.append(dict(zip(fields, row)))

    data[table] = rows

    with open('all_data.json', 'w') as outf:
        json.dump(data, outf, default=str)