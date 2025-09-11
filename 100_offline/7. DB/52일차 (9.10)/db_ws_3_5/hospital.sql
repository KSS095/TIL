USE hospital;

-- SELECT first_name, last_name, specialty
-- FROM doctor AS d
-- INNER JOIN visits AS v
-- ON d.doctor_id = v.doctor_id
-- WHERE specialty IN ('Neurology', 'Dermatology')
-- GROUP BY d.doctor_id
-- HAVING COUNT(*) >= 2;

SELECT first_name, last_name, specialty
FROM doctor
WHERE (doctor_id, specialty) IN (
    SELECT d.doctor_id, specialty
    FROM doctor AS d
    INNER JOIN visits AS v
    ON d.doctor_id = v.doctor_id
    WHERE specialty IN ('Neurology', 'Dermatology')
    GROUP BY d.doctor_id
    HAVING COUNT(*) >= 2
);

CREATE VIEW patient_visit_details
AS SELECT p.first_name AS patient_first_name, p.last_name AS patient_last_name,
          p.phone_number AS phone_number, v.visit_date AS visit_date,
          d.first_name AS doctor_first_name, d.last_name AS doctor_last_name, specialty
FROM visits AS v
INNER JOIN doctor AS d
ON v.doctor_id = d.doctor_id
INNER JOIN patient AS p
ON v.patient_id = p.patient_id;

CREATE VIEW doctor_patient_list
AS SELECT d.first_name AS doctor_first_name, d.last_name AS doctor_last_name,
          p.first_name AS patient_first_name, p.last_name AS patient_last_name,
          phone_number
FROM visits AS v
INNER JOIN doctor AS d
ON v.doctor_id = d.doctor_id
INNER JOIN patient AS p
ON v.patient_id = p.patient_id;

SELECT * FROM patient_visit_details;

SELECT * FROM doctor_patient_list
WHERE doctor_last_name = 'Brown';