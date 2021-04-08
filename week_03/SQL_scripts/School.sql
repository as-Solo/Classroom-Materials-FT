DROP DATABASE IF EXISTS school;
CREATE DATABASE school;
USE school;
​
​
CREATE TABLE teacher (
teacher_id INT PRIMARY KEY,
first_name VARCHAR(10) NOT NULL,
last_name VARCHAR(20) NOT NULL,
language_1 VARCHAR(3) NOT NULL,
languaje_2 VARCHAR(3) NOT NULL,
dob DATE,
tax_id INT,
phone_no VARCHAR(20)
);

CREATE TABLE client_ (
client_id INT PRIMARY KEY,
client_name VARCHAR(15) NOT NULL,
adress VARCHAR(40) NOT NULL,
industry VARCHAR(40) NOT NULL
);


CREATE TABLE company (
client_id INT PRIMARY KEY,
client_name VARCHAR (40) NOT NULL,
address VARCHAR (40) NOT NULL,
industry VARCHAR (40)
);
​
CREATE TABLE participant (
  participant_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  company INT
);
​
CREATE TABLE IF NOT EXISTS course (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(40) NOT NULL,
  language VARCHAR(3) NOT NULL,
  level VARCHAR(2),
  course_length_weeks INT,
  start_date DATE,
  in_school BOOLEAN,
  teacher INT,
  company INT
  );