USE recruitment_db;

SELECT username, title, location, application_date, status
FROM applications
INNER JOIN applicants
ON applications.applicant_id = applicants.id
INNER JOIN jobs
ON applications.job_id = jobs.id
WHERE username = 'john_doe';

SELECT username, email, phone, title, application_date
FROM applications
INNER JOIN applicants
ON applications.applicant_id = applicants.id
INNER JOIN jobs
ON applications.job_id = jobs.id
WHERE status = 'Accepted';

SELECT title, department, COUNT(*) AS applicant_count
FROM applications
INNER JOIN applicants
ON applications.applicant_id = applicants.id
INNER JOIN jobs
ON applications.job_id = jobs.id
WHERE title = 'Software Engineer'
GROUP BY department;

SELECT department, COUNT(*) AS pending_count
FROM applications
INNER JOIN applicants
ON applications.applicant_id = applicants.id
INNER JOIN jobs
ON applications.job_id = jobs.id
WHERE status = 'Pending'
GROUP BY department;