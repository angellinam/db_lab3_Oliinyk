
import psycopg2
import matplotlib.pyplot as plt

username = 'angelina'
password = 'angelina15'
database = 'Data Science Job Salaries'
host = 'localhost'
port = '1111'


query_1 = '''
    CREATE VIEW  AVGsalariesMiddleLvljob AS
    SELECT job_title, exp_id, ROUND(AVG(salary_usd)) AS avg_salary FROM jobs INNER JOIN salaries
    ON jobs.job_id = salaries.job_id
    WHERE exp_id = 'MI'
    GROUP BY  jobs.job_id, exp_id
    
'''

query_2 = '''
    CREATE VIEW  SalariesSeniorLvljobUSA AS
    SELECT job_title, exp_id, comp_id, salary_usd FROM jobs INNER JOIN salaries
    ON jobs.job_id = salaries.job_id
    WHERE exp_id = 'SE' AND comp_id = 'US'
    '''

query_3 = '''
    CREATE VIEW  SalariesMiddleLvljobGB AS
    SELECT job_title, exp_id, comp_id, salary_usd FROM jobs INNER JOIN salaries
    ON jobs.job_id = salaries.job_id
    WHERE exp_id = 'MI' and comp_id = 'GB' 
    ORDER BY salary_USD 
'''



conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)


with conn:
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS AVGsalariesMiddleLvljob')
    cur.execute(query_1)
    cur.execute('SELECT * FROM AVGsalariesMiddleLvljob')

    jobs = []
    salaries = []

    for row in cur:
        jobs.append(row[0])
        salaries.append(row[2])

    x_range = range(len(jobs))

    bar_ax.bar(x_range, salaries, width=0.9)
    bar_ax.set_title('Average salaries for each middle-level job')
    bar_ax.set_xlabel('Jobs')
    bar_ax.set_ylabel('Salary, $')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(jobs, rotation=80, ha='right', fontsize=8)

    cur.execute('DROP VIEW IF EXISTS SalariesSeniorLvljobUSA')
    cur.execute(query_2)
    cur.execute('SELECT * FROM SalariesSeniorLvljobUSA')

    jobs = []
    salaries = []

    for row in cur:
        jobs.append(row[0])
        salaries.append(row[3])

    pie_ax.pie(salaries, labels=jobs, autopct='%1.1f%%')
    pie_ax.set_title('Salaries for each senior-level job in the USA')

    cur.execute('DROP VIEW IF EXISTS SalariesMiddleLvljobGB')
    cur.execute(query_3)
    cur.execute('SELECT * FROM SalariesMiddleLvljobGB')

    jobs = []
    salaries = []

    for row in cur:
        jobs.append(row[0])
        salaries.append(row[3])

    graph_ax.plot(jobs, salaries, marker='o')
    graph_ax.set_xlabel('Jobs')
    graph_ax.set_ylabel('Salary, $')
    graph_ax.set_title('Salaries for each middle-level job in Great Britain')

    for job, salary in zip(jobs, salaries):
        graph_ax.annotate(salary, xy=(job, salary), xytext=(7, 2), textcoords='offset points')

mng = plt.get_current_fig_manager()
mng.resize(1600, 700)

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.9, wspace=0.4, hspace=0.4)

plt.show()
