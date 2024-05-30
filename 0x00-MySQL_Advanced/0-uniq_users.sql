-- SQL script that creates a table `users` with the necessary requirements
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
);
