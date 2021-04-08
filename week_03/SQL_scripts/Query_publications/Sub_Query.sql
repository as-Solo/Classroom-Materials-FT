SELECT SUM(`TITLE COUNT`) FROM
-- Toda esta sentencia SELECT entre paréntesis es sólo nuestra tabla
(SELECT a.au_id AS 'AUTHOR ID', au_lname AS 'LAST NAME', au_fname AS 'FIRST NAME', 
       pub_name AS 'PUBLISHER', COUNT(t.title_id) AS 'TITLE COUNT'
FROM authors AS a
    JOIN titleauthor AS ta
        ON a.au_id = ta.au_id
    JOIN titles AS t
        ON t.title_id = ta.title_id
    JOIN publishers AS p
        ON t.pub_id = p.pub_id
GROUP BY p.pub_id, a.au_id) AS title_count;