-- script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
Select COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT From INFORMATION_SCHEMA.COLUMNS Where TABLE_NAME = 'first_table';
