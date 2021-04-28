-- SQL script that creates a table users
-- Attributes id, email, name
CREATE DATABASE IF NOT EXISTS holberton;
USE holberton;
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	email VARCHAR(256) NOT NULL UNIQUE,
	name VARCHAR(256))
