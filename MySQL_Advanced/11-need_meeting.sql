-- 11. No table for a meeting
-- Creates a view need_meeting that lists all students with score < 80 and no last_meeting or last_meeting > 1 month ago
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
