USE movies;

SELECT * FROM movie_list
WHERE release_year BETWEEN 2000 AND 2010;

SELECT * FROM movie_list
WHERE title BETWEEN 'A' AND 'M';

SELECT * FROM movie_list
WHERE genre = 'Drama'
  AND release_year BETWEEN 1990 AND 2000;

SELECT * FROM movie_list
WHERE release_year BETWEEN 2015 AND 2020
  AND (genre = 'Sci-Fi' OR genre = 'Action');

SELECT * FROM movie_list
WHERE release_year BETWEEN 2006 AND 2014;