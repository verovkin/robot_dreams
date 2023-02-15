-- 5. Написати запит, який виведе кількість покупок книжок для автора Rowling.
-- Результат має бути представлений у форматі: amount

SELECT COUNT(*) AS amount FROM purchases
INNER JOIN books ON purchases.book_id = books.id WHERE books.author = 'Rowling';