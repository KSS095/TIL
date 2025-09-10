USE online_course_platform_db;

SELECT feedback.comment
FROM feedback
INNER JOIN students
ON feedback.student_id = students.id
WHERE students.username = 'john_doe'
  AND feedback.created_at = (SELECT min(created_at) FROM feedback);

CREATE VIEW student_feedback_with_courses
AS
SELECT s.username AS username, c.title AS course_title, f.comment AS comment, f.created_at AS created_at
FROM feedback AS f
INNER JOIN students AS s
ON f.student_id = s.id
INNER JOIN courses AS c
ON f.course_id = c.id;

SELECT *
FROM student_feedback_with_courses
WHERE username = 'john_doe';