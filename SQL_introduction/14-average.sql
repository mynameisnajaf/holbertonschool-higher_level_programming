-- Computes the score average of all records in the table
INSERT INTO second_table (average) SELECT AVG(score) FROM second_table;
