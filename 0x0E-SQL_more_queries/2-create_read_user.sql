-- A script that creates the database hbtn_0d_2 and the user user_0d_2
--  - user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
--  - The user_0d_2 password should be set to user_0d_2_pwd
--  - If the database hbtn_0d_2 already exists, your script should not fail
--  - If the user user_0d_2 already exists, your script should not fail
IF EXISTS(SELECT * from sys.databases WHERE name='hbtn_0d_2')
BEGIN
    DROP DATABASE hbtn_0d_2;
END

CREATE DATABASE hbtn_0d_2;

ALTER USER 'user_0d_2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2 TO 'user_0d_2'@'localhost' WITH GRANT OPTION;;
