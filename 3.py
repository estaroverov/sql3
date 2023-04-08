import mysql.connector as msql

# Функция вывода результата запроса

def print_query_result(result):
    for row in result:
        print(row)
    print()
    return


connector = msql.connect(user='root', password='',
                              host='localhost',
                              database='db')

cursor = connector.cursor()
query = "CREATE TABLE staff (\
	id INT AUTO_INCREMENT PRIMARY KEY, \
	firstname VARCHAR(45),\
	lastname VARCHAR(45),\
	post VARCHAR(100),\
	seniority INT, \
	salary INT, \
	age INT );"
cursor.execute(query)

query = "INSERT INTO staff (firstname, lastname, post, seniority, salary, age)\
VALUES\
('Вася', 'Петров', 'Начальник', '40', 100000, 60),\
('Петр', 'Власов', 'Начальник', '8', 70000, 30),\
('Катя', 'Катина', 'Инженер', '2', 70000, 25),\
('Саша', 'Сасин', 'Инженер', '12', 50000, 35),\
('Иван', 'Иванов', 'Рабочий', '40', 30000, 59),\
('Петр', 'Петров', 'Рабочий', '20', 25000, 40),\
('Сидр', 'Сидоров', 'Рабочий', '10', 20000, 35),\
('Антон', 'Антонов', 'Рабочий', '8', 19000, 28),\
('Юрий', 'Юрков', 'Рабочий', '5', 15000, 25),\
('Максим', 'Максимов', 'Рабочий', '2', 11000, 22),\
('Юрий', 'Галкин', 'Рабочий', '3', 12000, 24),\
('Людмила', 'Маркина', 'Уборщик', '10', 10000, 49);"
cursor.execute(query)
connector.commit()

# Отсортируйте данные по полю заработная плата (salary) в порядке: убывания; возрастания
query = "SELECT * FROM staff ORDER BY salary DESC;"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

query = "SELECT * FROM staff ORDER BY salary;"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

# Выведите 5 максимальных заработных плат (saraly)
query = "SELECT * FROM staff ORDER BY salary DESC LIMIT 5;"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

# Посчитайте суммарную зарплату (salary) по каждой специальности (роst)
query = "SELECT post, SUM(salary) AS sum_salary FROM staff GROUP BY post;"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

# Найдите кол-во сотрудников с специальностью (post) «Рабочий» в возрасте от 24 до 49 лет включительно.
query = "SELECT COUNT(*) AS count_staff FROM staff WHERE post = 'Рабочий' AND age BETWEEN 24 AND 49;"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

# Найдите количество специальностей
query = "SELECT  COUNT(DISTINCT post) FROM staff;"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

# Выведите специальности, у которых средний возраст сотрудников меньше 30 лет
query = "SELECT post, AVG(age) FROM staff GROUP BY post HAVING AVG(age)>30"
cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

cursor.close()
connector.close()
