Use recruitment_db;

ALTER TABLE applicants
ADD INDEX idx_applicants_username(username);

ALTER TABLE jobs
ADD INDEX idx_jobs_department(department);

ALTER TABLE applications
ADD INDEX idx_applications_application_date(application_date);

ALTER TABLE applications
ADD INDEX idx_applications_status(status);

SELECT username, title, location, application_date, status
FROM applications AS t
INNER JOIN applicants AS c
ON t.applicant_id = c.id
INNER JOIN jobs AS j
ON t.job_id = j.id
WHERE username = 'john_doe';

SELECT department, COUNT(*) AS pending_count
FROM applications AS t
INNER JOIN applicants AS c
ON t.applicant_id = c.id
INNER JOIN jobs AS j
ON t.job_id = j.id
GROUP BY department

SELECT username, email, phone, title, location, application_date, status
FROM applications AS t
INNER JOIN applicants AS c
ON t.applicant_id = c.id
INNER JOIN jobs AS j
ON t.job_id = j.id
WHERE application_date >= '2023-08-01'
  AND status = 'Reviewed';

CREATE VIEW applicant_job_applications
AS SELECT username, title AS job_title, department, location, application_date, status
FROM applications AS t
INNER JOIN applicants AS c
ON t.applicant_id = c.id
INNER JOIN jobs AS j
ON t.job_id = j.id;

SELECT * FROM applicant_job_applications
WHERE username = 'jane_smith';