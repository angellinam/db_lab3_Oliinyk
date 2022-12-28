DO $$
 DECLARE 
 	 job          salaries.job_id%TYPE;
	 experience   salaries.exp_id%TYPE;
	 company      salaries.comp_id%TYPE;
     salary       salaries.salary_usd%TYPE;
     
 BEGIN
     salary := 10000;
     job := 'job_';
	 experience := 'exp_';
	 company := 'company_';
     FOR counter IN 1..20
         LOOP
             INSERT INTO salaries(job_id, exp_id, comp_id, salary_usd)
             VALUES (job || 0+counter, experience || 100+counter, company || 0+counter, counter + salary);
         END LOOP;
 END;
 $$