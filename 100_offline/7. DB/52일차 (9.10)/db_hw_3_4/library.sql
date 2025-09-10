USE library_db;

SELECT books.title AS BookTitle, authors.name AS AuthorName, genres.genre_name AS GenreName
FROM books
INNER JOIN authors
    ON books.author_id = authors.id
INNER JOIN genres
    ON books.genre_id = genres.id;

ALTER TABLE authors
ADD INDEX idx_authors_name (name);

ALTER TABLE genres
ADD INDEX idx_genres_genre_name (genre_name);

SELECT books.title AS book_title, authors.name AS author_name, genres.genre_name AS genre_name
FROM books
INNER JOIN authors
    ON books.author_id = authors.id
INNER JOIN genres
    ON books.genre_id = genres.id
WHERE authors.name = 'J.K.Rowling'
  AND genres.genre_name = 'Fantasy';
