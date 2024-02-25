-- STUDENT

CREATE TABLE COURSE (
  course_number VARCHAR(8) PRIMARY KEY,
  course_name VARCHAR(25) NOT NULL UNIQUE,
  department VARCHAR(4) NOT NULL,
  credit_hours CHAR(1) NOT NULL
);

CREATE TABLE SECTION (
  section_identifier VARCHAR(3) PRIMARY KEY,
  course_number FOREIGN KEY REFERENCES COURSE(course_number),
  semester VARCHAR(6) NOT NULL,
  year CHAR(2) NOT NULL,
  instructor VARCHAR(8) NOT NULL
);

CREATE TABLE STUDENT (
  student_number VARCHAR(2) PRIMARY KEY,
  name VARCHAR(20) NOT NULL,
  class CHAR(1) NOT NULL,
  major CHAR(2)
);

CREATE TABLE GRADE_REPORT (
  student_number VARCHAR(3) PRIMARY KEY,
  section_identifier VARCHAR(3) PRIMARY KEY,
  grade CHAR(1) NOT NULL
);

CREATE TABLE PREREQUISITE (
  prerequisite_number VARCHAR(8) PRIMARY KEY,
  course_number VARCHAR(6) NOT NULL
);