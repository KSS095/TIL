CREATE DATABASE hospital
    DEFAULT CHARACTER SET = 'utf8mb4';

USE hospital;

CREATE TABLE patient(
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    phone_number VARCHAR(15)
);

INSERT INTO patient(patient_id, first_name, last_name, birth_date, phone_number)
VALUES
    (1, 'John', 'Doe', '1990-01-01', '123-456-7890'),
    (2, 'Jane', 'Smith', '1985-02-02', '098-765-4321'),
    (3, 'Alice', 'White', '1970-03-15', '111-222-3333');

CREATE TABLE doctor(
    doctor_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialty VARCHAR(100)
);

INSERT INTO doctor(doctor_id, first_name, last_name, specialty)
VALUES
    (1, 'Alice', 'Brown', 'Cardiology'),
    (2, 'Bob', 'Johnson', 'Neurology'),
    (3, 'Charlie', 'Davis', 'Dermatology');

CREATE TABLE visits(
    visit_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
    visit_date DATE
);

INSERT INTO visits(visit_id, patient_id, doctor_id, visit_date)
VALUES
    (1, 1, 1, '2024-01-01'),
    (2, 2, 2, '2024-02-01'),
    (3, 1, 2, '2024-03-01'),
    (4, 3, 3, '2024-04-01'),
    (5, 1, 2, '2024-05-01'),
    (6, 2, 3, '2024-06-01'),
    (7, 3, 1, '2024-07-01');

SELECT p.first_name AS first_name, p.last_name AS last_name, p.phone_number AS phone_number, v.visit_date AS visit_date, d.first_name AS doctor_first_name, d.last_name AS doctor_last_name, d.specialty AS specialty
FROM visits AS v
INNER JOIN doctor AS d
ON v.doctor_id = d.doctor_id
INNER JOIN patient AS p
ON v.patient_id = p.patient_id;

SELECT d.first_name AS first_name, d.last_name AS last_name,
       d.specialty AS specialty, COUNT(d.doctor_id) AS visit_count
FROM visits AS v
INNER JOIN doctor AS d
ON v.doctor_id = d.doctor_id
INNER JOIN patient AS p
ON v.patient_id = p.patient_id
GROUP BY d.doctor_id;

SELECT p.first_name AS first_name, p.last_name AS last_name,
       p.phone_number AS phone_number, COUNT(*) AS visit_count
FROM visits AS v
INNER JOIN doctor AS d
ON v.doctor_id = d.doctor_id
INNER JOIN patient AS p
ON v.patient_id = p.patient_id
WHERE d.doctor_id = 2
GROUP BY p.patient_id, p.first_name, p.last_name, p.phone_number
HAVING COUNT(*) >= 2;