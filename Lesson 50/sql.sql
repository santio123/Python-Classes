CREATE TABLE Marks (
    roll_no NUMBER,
    subject TEXT,
    marks REAL
);

INSERT INTO Marks VALUES
(1, 'Math', 85),
(1, 'Science', 78),
(2, 'Math', 92),
(2, 'Science', 88),
(3, 'Math', 70);

SELECT * FROM Marks;

SELECT MIN(marks)
FROM Marks;

SELECT MAX(marks)
FROM Marks;

SELECT AVG(marks)
FROM Marks;

SELECT SUM(marks)
FROM Marks;
