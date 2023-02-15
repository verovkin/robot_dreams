-- 7. (необов'язкове виконання) Написати запит, який виведе загальні суми продажів
-- для кожного автора та кількість покупок.

SELECT books.author, SUM(books.price) AS purchase_sum, COUNT(*) AS total_purchases FROM purchases
INNER JOIN books ON books.id = purchases.book_id
GROUP BY books.author;