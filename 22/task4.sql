-- 4. Написати запит, який виведе кількість покупок книжок для кожного user.
-- Результат має бути представлений у форматі: user.id (http://user.id/), purchases_count

SELECT purchases.user_id, COUNT(*) AS purchases_count FROM purchases GROUP BY purchases.user_id;