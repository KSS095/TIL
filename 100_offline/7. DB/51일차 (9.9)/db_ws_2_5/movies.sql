-- Active: 1753408150587@@127.0.0.1@3306@movies
USE movies;

SELECT genre FROM movie_list
GROUP BY genre
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT genre, COUNT(*) AS movie_count, AVG(release_year) AS avg_release_year
FROM movie_list
GROUP BY genre;

SELECT m1.genre, m1.title, m1.release_year
FROM movie_list m1
JOIN(SELECT genre, MAX(release_year) AS max_year
      FROM movie_list
      GROUP BY genre) AS m2
ON m1.genre = m2.genre AND m1.release_year = m2.max_year;


SELECT * FROM movie_list
WHERE release_year = (SELECT MIN(release_year)
                      FROM movie_list
                      WHERE genre = 'Action')
  and genre NOT IN ('Action')
ORDER BY release_year, title;

SELECT * FROM movie_list
WHERE release_year IN (SELECT release_year
                        FROM movie_list
                        WHERE genre = 'Drama')
  and (genre = 'Sci-Fi' or genre = 'Action')
ORDER BY release_year;