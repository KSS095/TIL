CREATE DATABASE hospital_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE hospital_db;

CREATE TABLE patients(
  hospital_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(150) NOT NULL,
  location VARCHAR(200) NOT NULL,
  established_date DATE,
  contact_number VARCHAR(20) UNIQUE,
  type VARCHAR(50) NOT NULL
);

ALTER TABLE patients
ADD COLUMN capacity INT;

ALTER TABLE patients
MODIFY COLUMN type VARCHAR(100);

ALTER TABLE patients
RENAME COLUMN established_date TO founded_date

DROP TABLE patients;