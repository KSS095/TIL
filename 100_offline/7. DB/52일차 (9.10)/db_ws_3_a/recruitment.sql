CREATE DATABASE recruitment_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE recruitment_db;
 
CREATE TABLE applicants(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100),
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

INSERT INTO applicants(username, name, email, phone)
VALUES
    ('john_doe', 'John Doe', 'john@example.com', '123-456-7890'),
    ('jane_smith', 'Jane Smith', 'jane@example.com', '234-567-8901'),
    ('mary_jones', 'Mary Jones', 'mary@example.com', '345-678-9012'),
    ('paul_brown', 'Paul Brown', 'paul@example.com', '456-789-0123'),
    ('lisa_white', 'Lisa White', 'lisa@example.com', '567-890-1234');
 
CREATE TABLE jobs(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    department VARCHAR(100),
    location VARCHAR(100)
);

INSERT INTO jobs(title, department, location)
VALUES
    ('Software Engineer', 'Engineering', 'New York'),
    ('Data Scientist', 'Data Science', 'San Francisco'),
    ('Product Manager', 'Product', 'Boston'),
    ('UX Designer', 'Design', 'Los Angeles'),
    ('Marketing Specialist', 'Marketing', 'Chicago');

CREATE TABLE applications(
    id INT PRIMARY KEY AUTO_INCREMENT,
    applicant_id INT,
    job_id INT,
    FOREIGN KEY (applicant_id) REFERENCES applicants(id),
    FOREIGN KEY (job_id) REFERENCES jobs(id),
    application_date DATE,
    status ENUM('Pending', 'Reviewed', 'Accepted', 'Rejected')
);

INSERT INTO applications(applicant_id, job_id, application_date, status)
VALUES
    (1, 1, '2023-08-01', 'Pending'),
    (2, 2, '2023-08-02', 'Reviewed'),
    (3, 3, '2023-08-03', 'Accepted'),
    (4, 4, '2023-08-04', 'Rejected'),
    (5, 5, '2023-08-05', 'Pending');
