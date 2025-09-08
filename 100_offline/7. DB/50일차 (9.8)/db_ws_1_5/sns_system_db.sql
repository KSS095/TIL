CREATE DATABASE sns_system_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE sns_system_db;

CREATE TABLE USER(
  userid INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(20),
  email VARCHAR(50)
)

CREATE TABLE ARTICLE(
  articleid INT PRIMARY KEY AUTO_INCREMENT,
  userid INT,
  FOREIGN KEY (userid) REFERENCES USER(userid),
  title VARCHAR(50),
  content VARCHAR(50)
)

CREATE TABLE COMMENT(
  commentid INT PRIMARY KEY AUTO_INCREMENT,
  articleid INT,
  FOREIGN KEY (articleid) REFERENCES ARTICLE(articleid),
  content VARCHAR(50)
)


INSERT INTO USER
VALUES
(1, '홍길동', 'hong@example.com'),
(2, '이순신', 'lee@example.com')

INSERT INTO ARTICLE
VALUES
(101, 1, '첫 번째 게시물', '안녕하세요'),
(102, 1, '두 번째 게시물', '반갑습니다'),
(103, 2, '세 번째 게시물', '좋은 하루')

INSERT INTO COMMENT
VALUES
(1001, 101, '첫 댓글'),
(1002, 102, '두 번째 댓글'),
(1003, 103, '세 번째 댓글')

SELECT name, email FROM USER;

SELECT title, content
FROM USER JOIN ARTICLE
WHERE USER.userid = ARTICLE.userid and USER.name = '홍길동';

SELECT COMMENT.content
FROM ARTICLE JOIN COMMENT
WHERE ARTICLE.articleid = COMMENT.articleid
  AND ARTICLE.title = '첫 번째 게시물';

INSERT INTO USER
VALUES(3, '김유신', 'kim@example.com');

SELECT * FROM USER;

UPDATE USER
SET email = 'new_lee@example.com'
WHERE name = '이순신'

SELECT * FROM USER;