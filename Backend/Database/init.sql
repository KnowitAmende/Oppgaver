CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year_published INT NOT NULL,
    genre VARCHAR(255) NOT NULL
);

INSERT INTO books (title, author, year_published, genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('Pride and Prejudice', 'Jane Austen', 1813, 'Romance'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Tragedy'),
('Moby Dick', 'Herman Melville', 1851, 'Adventure'),
('War and Peace', 'Leo Tolstoy', 1869, 'Historical'),
('The Catcher in the Rye', 'J.D. Salinger', 1951, 'Fiction'),
('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy'),
('Fahrenheit 451', 'Ray Bradbury', 1953, 'Dystopian'),
('Jane Eyre', 'Charlotte Bronte', 1847, 'Romance'),
('Brave New World', 'Aldous Huxley', 1932, 'Dystopian'),
('Animal Farm', 'George Orwell', 1945, 'Political satire'),
('The Odyssey', 'Homer', -800, 'Epic'),
('Les Misérables', 'Victor Hugo', 1862, 'Historical'),
('The Brothers Karamazov', 'Fyodor Dostoevsky', 1880, 'Philosophical'),
('Crime and Punishment', 'Fyodor Dostoevsky', 1866, 'Psychological'),
('The Count of Monte Cristo', 'Alexandre Dumas', 1844, 'Adventure'),
('Wuthering Heights', 'Emily Bronte', 1847, 'Tragedy'),
('Great Expectations', 'Charles Dickens', 1861, 'Bildungsroman'),
('The Picture of Dorian Gray', 'Oscar Wilde', 1890, 'Philosophical');
