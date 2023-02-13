-- task 4
SELECT age, COUNT(age) AS users FROM users GROUP BY age ORDER BY users DESC, age