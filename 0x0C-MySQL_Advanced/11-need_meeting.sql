-- iew need_meeting that lists all students
-- that have a score under 80 and no last meeting
CREATE VIEW need_meeting AS SELECT name FROM students WHERE score < 80
AND NOT last_meeting OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH);