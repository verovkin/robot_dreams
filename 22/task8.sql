-- 8. (необов'язкове виконання) Написати запит, який виведе всі назви книжок із кількістью
-- їх продажів в порядку спадання кількості продажів.

SELECT books.title, COUNT(purchases.book_id) AS amount FROM books
LEFT JOIN purchases ON books.id = purchases.book_id
GROUP BY books.id
ORDER BY amount DESC;