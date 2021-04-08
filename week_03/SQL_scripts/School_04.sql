INSERT INTO teacher VALUES
(1, 'James', 'Smith', 'ENG', 'SPA', '1985-04-20', 12345, '+491774553676');

#DELETE FROM teacher WHERE teacher_id = 2;

UPDATE teacher
SET last_name = 'Jones'
WHERE teacher_id = 1;