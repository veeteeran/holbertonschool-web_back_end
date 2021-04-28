-- SQL script that creates a table users
-- Attributes id, email, name
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	email VARCHAR(256) NOT NULL UNIQUE,
	name VARCHAR(256),
	country ENUM('US', 'CO', 'TN') NOT NULL)
