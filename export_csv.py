import csv
import psycopg2

username = 'angelina'
password = 'angelina15'
database = 'Data Science Job Salaries'
host = 'localhost'
port = '1111'


OUTPUT_FILE_T = 'Data_Science_Job_Salaries.csv'

TABLES = [
    'jobs',
    'experiencelevels',
    'companieslocation',
    'salaries',
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])