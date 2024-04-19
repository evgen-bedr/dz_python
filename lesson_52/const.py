dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'sakila'}

QUERY_CATEGOTIES = 'SELECT category_id, name FROM category'

QUERY_FILMS = """
SELECT film.film_id, film.title, film.release_year, film.description
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.category_id = {} LIMIT 10;
"""


QUERY_FILM_DETAILS = """
SELECT f.*, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.film_id = {}
"""
