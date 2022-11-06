-- Script that creates a table 'second_table' in the database 'hbtn_0c_0' in my MySQL server and adds multiple rows
-- Description of 'second_table': id = INT, name = VARCHAR(256), score = INT
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT);
-- Adds row for John
INSERT INTO  second_table (id, name, score) VALUES (1, "John", 10);
-- Adds row for Alex
INSERT INTO  second_table (id, name, score) VALUES (2, "Alex", 3);
-- Adds row for Bob
INSERT INTO  second_table (id, name, score) VALUES (3, "Bob", 14);
-- Adds row for George
INSERT INTO  second_table (id, name, score) VALUES (4, "George", 8);