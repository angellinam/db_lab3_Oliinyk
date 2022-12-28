CREATE TABLE Jobs(
	job_id varchar(50) NOT NULL,
	job_title varchar(50) NOT NULL,
	PRIMARY KEY(job_id)	
);

CREATE TABLE CompaniesLocation(
	comp_id varchar(20) NOT NULL,
	comp_location varchar(20) NOT NULL,
	PRIMARY KEY(comp_id)	
);

CREATE TABLE ExperienceLevels(
	exp_id varchar(30) NOT NULL,
	exp_lvl varchar(30) NOT NULL,
	PRIMARY KEY(exp_id)	
);

CREATE TABLE Salaries(
	job_id varchar(50) NOT NULL,
	exp_id varchar(30) NOT NULL,
	comp_id varchar(20) NOT NULL,
	salary_USD INT NOT NULL,
	PRIMARY KEY(job_id,exp_id,comp_id),
	CONSTRAINT FK_job FOREIGN KEY(job_id) REFERENCES Jobs(job_id),
	CONSTRAINT FK_exp_lvl FOREIGN KEY(exp_id) REFERENCES ExperienceLevels(exp_id),
	CONSTRAINT FK_comp FOREIGN KEY(comp_id) REFERENCES CompaniesLocation(comp_id)
);