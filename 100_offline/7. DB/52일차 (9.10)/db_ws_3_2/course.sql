USE online_course_platform_db;

SELECT students.username AS username, courses.title AS course_title, feedback.comment AS comment
FROM feedback
INNER JOIN courses
ON feedback.student_id = courses.id
INNER JOIN students
ON feedback.student_id = students.id
WHERE students.username = 'john_doe';

SELECT students.username AS username, courses.title AS course_title, feedback.comment AS comment
FROM feedback
LEFT JOIN courses
ON feedback.student_id = courses.id
LEFT JOIN students
ON feedback.student_id = students.id
WHERE students.username = 'jane_smith';

SELECT feedback.comment
FROM feedback
INNER JOIN students
ON feedback.student_id = students.id
WHERE students.username = 'mary_jones';