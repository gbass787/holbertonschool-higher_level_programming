-- Script that creates the table 'force_name' on my MySQL server
-- Description for 'force_name': id = int, name = VARCHAR(256)
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL);