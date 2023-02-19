-- 3. Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували,
-- відсортувати дані за user_id. Результат має бути представлений у форматі: users.id (http://users.id/),
-- users.first_name, users.last_name, books.title

SELECT users.id, users.first_name, users.last_name, books.title FROM purchases
INNER JOIN users ON users.id = purchases.user_id
INNER JOIN books ON books.id = purchases.book_id
ORDER BY users.id;