-- task 5
SELECT age, COUNT(age) AS users FROM users GROUP BY age HAVING users > 1 ORDER BY users DESC, age