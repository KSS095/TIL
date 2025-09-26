-- Active: 1752638634287@@127.0.0.1@3306@pjt04_db
create database pjt04_db;

USE pjt04_db;

CREATE TABLE chuseok_holiday (
    year INT PRIMARY KEY,              -- 연도
    start_date DATE NOT NULL,          -- 추석 연휴 시작일
    end_date DATE NOT NULL,            -- 추석 연휴 종료일
    start_day VARCHAR(10) NOT NULL,    -- 시작 요일
    end_day VARCHAR(10) NOT NULL       -- 종료 요일
);

INSERT INTO chuseok_holiday (year, start_date, end_date, start_day, end_day)
VALUES
(2022, '2022-09-08', '2022-09-12', '목', '월'),
(2023, '2023-09-27', '2023-10-03', '수', '화'),
(2024, '2024-09-13', '2024-09-18', '금', '수');

ALTER TABLE chuseok_holiday
ADD COLUMN holiday_days INT;

UPDATE chuseok_holiday
SET holiday_days = DATEDIFF(end_date, start_date) + 1;

ALTER TABLE chuseok_holiday
ADD COLUMN holiday_main DATE;

UPDATE chuseok_holiday
SET holiday_main = '2022-09-10'
WHERE year = 2022;

UPDATE chuseok_holiday
SET holiday_main = '2023-09-29'
WHERE year = 2023;

UPDATE chuseok_holiday
SET holiday_main = '2024-09-17'
WHERE year = 2024;

