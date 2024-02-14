-- A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
IF EXISTS(SELECT * from sys.databases WHERE name='hbtn_0d_usa') 
BEGIN 
    DROP DATABASE hbtn_0d_usa;
END 

CREATE DATABASE hbtn_0d_usa;
GO

USE hbtn_0d_usa;
GO

CREATE TABLE states(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
