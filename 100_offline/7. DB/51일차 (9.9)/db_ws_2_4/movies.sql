-- Active: 1753408150587@@127.0.0.1@3306@movies
USE movies;

INSERT INTO movie_list(title, genre, release_year)
VALUES
  ('The Matrix', 'Sci-Fi', 1999),
  ('Gladiator', 'Action', 2000),
  ('Jurassic Park', 'Sci-Fi', 1993),
  ('The Fugitive', 'Action', 1993);

SELECT title FROM movie_list
WHERE release_year = (SELECT MIN(release_year)
                       FROM movie_list
                        WHERE genre = 'Drama');

SELECT title, release_year FROM movie_list
WHERE genre = 'Action'
  and release_year = (SELECT MAX(release_year)
                        FROM movie_list
                        WHERE release_year >= 2000);

SELECT * FROM movie_list
WHERE release_year IN (SELECT release_year FROM movie_list
                        WHERE genre = 'Drama')
  and (genre = 'Sci-Fi' or genre = 'Action');


SELECT * FROM movie_list
WHERE release_year >= (SELECT AVG(release_year) FROM movie_list
                        WHERE genre = 'Action')
  and genre = 'Sci-Fi';


SELECT * FROM movie_list
WHERE release_year = (SELECT MIN(release_year) FROM movie_list
                      WHERE genre = 'Action')
  and genre NOT IN ('ACTION');
