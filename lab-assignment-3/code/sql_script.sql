use mysql;
CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON *.* TO 'test_user'@'localhost';
flush privileges;

SELECT 'New User named test_user created successfully.' as '';

CREATE DATABASE phone_directory;
USE phone_directory;
CREATE TABLE contacts(id int PRIMARY KEY auto_increment, name varchar(255) NOT NULL, mobile_no varchar(10) NOT NULL, email varchar(255) NOT NULL);
show tables;
