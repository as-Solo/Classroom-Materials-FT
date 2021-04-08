SELECT * FROM employees


SELECT birth_date, first_name FROM employees

SELECT birth_date, first_name FROM employees WHERE first_name = 'Hugo'

SELECT * FROM employees WHERE first_name = 'Hugo' AND gender = 'F'

SELECT * FROM employees WHERE first_name = 'Hugo' OR gender = 'F'

SELECT * FROM employees WHERE first_name = 'Hugo' AND gender = 'F' OR gender = 'M'

# ESTAS DOS QUERYs SON IDÉNTICAS##################################################################
SELECT * FROM employees WHERE first_name = 'Hugo' OR first_name = 'Bojan' or first_name = 'Anneke'

SELECT * FROM employees WHERE first_name IN ('Hugo', 'Bojan', 'Anneke')
##################################################################################################

SELECT * FROM employees WHERE first_name NOT IN ('Hugo', 'Bojan', 'Anneke')

SELECT * FROM employees WHERE first_name LIKE ('An%') # El símbolo % es como decir 'cualquier cosa' por lo tento, devolverá todo lo que empiece por An

SELECT * FROM employees WHERE first_name LIKE('mar_') # La barra baja hará lo mismo que el % pero con solo un caracter

SELECT * FROM employees WHERE first_name LIKE('_ary')

SELECT * FROM employees WHERE hire_date NOT LIKE ('1990%')

# ESTAS DOS QUERYs SON IDÉNTICAS##################################################################
SELECT * FROM employees WHERE hire_date >= '1990-01-01' AND hire_date <= '2000-01-01' 

SELECT * FROM employees WHERE hire_date BETWEEN '1990-01-01' AND '2000-01-01' 
##################################################################################################

SELECT * FROM salaries WHERE salary NOT BETWEEN 60000 AND 70000

SELECT * FROM employees WHERE first_name BETWEEN 'A%' AND 'D%'

SELECT * FROM employees WHERE gender = 'F' AND hire_date > '2000-01-01'

SELECT gender FROM employees

SELECT DISTINCT gender FROM employees

SELECT COUNT(emp_no) FROM employees

SELECT COUNT(DISTINCT first_name) FROM employees

SELECT COUNT(*)
FROM employees
WHERE birth_date >= '1965-01-01'

SELECT *
FROM employees
ORDER BY first_name ASC

SELECT *
FROM employees
ORDER BY first_name DESC

SELECT MAX(salary)
FROM salaries

SELECT AVG(salary)
FROM salaries

SELECT COUNT(DISTINCT dept_no)
FROM dept_emp

SELECT first_name, COUNT(first_name) AS count_name  # se pueden usar alias para modificar el nombre de visualización
FROM employees
GROUP BY first_name
HAVING count_name > 250   # esto es como un where, porque el WHERE aquí no funciona
ORDER BY first_name

SELECT CONCAT(first_name, ' ', last_name) as full_name
FROM employees

SELECT emp_no, salary
FROM salaries
LIMIT 10

SELECT first_name, SUM(first_name) FROM employees