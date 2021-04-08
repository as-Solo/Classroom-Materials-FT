SELECT pub_name, COUNT(title_id) AS count_titles
FROM publishers
INNER JOIN titles
ON publishers.pub_id = titles.pub_id
GROUP BY pub_name


SELECT pub_name, COUNT(title_id) AS count_titles
FROM publishers
LEFT JOIN titles
ON publishers.pub_id = titles.pub_id
GROUP BY pub_name

SELECT pub_name, title
FROM publishers
INNER JOIN titles
ON publishers.pub_id = titles.pub_id

SELECT pub_name, title
FROM publishers
LEFT JOIN titles
ON publishers.pub_id = titles.pub_id


################################### EL GROUP BY AGRUPA LOS VALORES ####################
SELECT *
FROM publishers
GROUP BY country
#######################################################################################

SELECT title, type, price, SUM(qty) AS units_sold
FROM sales
RIGHT JOIN titles
ON sales.title_id = titles.title_id
GROUP BY title

