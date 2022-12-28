import csv
import psycopg2

username = 'angelina'
password = 'angelina15'
database = 'Data Science Job Salaries'
host = 'localhost'
port = '1111'

INPUT_CSV_FILE = 'ds_salaries.csv'


query_delete = '''
DELETE FROM jobs;
DELETE FROM experiencelevels;
DELETE FROM companieslocation;
DELETE FROM salaries;
'''

insert_jobs = '''
INSERT INTO jobs (job_id, job_title) VALUES (%s, %s)
'''

insert_exp = '''
INSERT INTO experiencelevels (exp_id, exp_lvl) VALUES (%s, %s)
'''

insert_comp = '''
INSERT INTO companieslocation (comp_id, comp_location) VALUES (%s, %s)
'''

insert_salary = '''
INSERT INTO salaries (job_id, exp_id, comp_id, salary_usd) VALUES (%s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()
    cur.execute(query_delete)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        jobs = []
        experience = []
        company = []
        salary = [[]]
        idx = 0
        for idx, row in enumerate(reader):
            if jobs.count(row['job_title']) == 0:
                jobs.append(row['job_title'])
                cur.execute(insert_jobs, (row['job_title'], row['job_title']))
            if experience.count(row['experience_level']) == 0:
               experience.append(row['experience_level'])
               cur.execute(insert_exp, (row['experience_level'], row['experience_level']))
            if company.count(row['company_location']) == 0:
                company.append(row['company_location'])
                cur.execute(insert_comp, (row['company_location'], row['company_location']))
            if salary.count([row['job_title'], row['experience_level'], row['company_location']]) == 0:
                salary.append([row['job_title'], row['experience_level'], row['company_location']])
                cur.execute(insert_salary, (row['job_title'], row['experience_level'], row['company_location'], row['salary_in_usd']))
    conn.commit()