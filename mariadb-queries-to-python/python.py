# ************************** Correr os queries de bases de dados do ficheiro myMariaDB.py ********************************

# Desenvolva um programa que utilize uma ligação à base de dados 
# Obtenha o output dos queries
# Utilize um módulo separado para o tratamento dos acessos e processamento relacionado com a base de dados. 
# O módulo principal terá apenas a definição dos queries a correr e receber de volta os resultados - tudo o que fôr relacionado com base de dados fica no módulo respectivo.

# ************************** Correr os queries de bases de dados do ficheiro myMariaDB.py ********************************

# Fazemos import do myMariaDB
from myMariaDB import *


# para criar uma query com várias linhas numa única string, iniciamo-la com 3 aspas e fechamo-la com 3 aspas
# query 1
s1 = """select distinct
concat ( employees.last_name , ", " , first_name ) as "Employee Last, First Name",
birth_date as "Birth Date",
employees.emp_no,
dept_name as "Department Name",
sum(salaries.salary) as "Salary Total"
from employees , salaries , departments , dept_emp
where employees.emp_no = salaries.emp_no
and departments.dept_no = dept_emp.dept_no
and dept_emp.emp_no = employees.emp_no
and employees.emp_no like '2667_'
group by 1 , 2 , 3 , 4 
order by birth_date desc
limit 500;"""

# query 2
s2 = """select
employees.emp_no as "Employee Number",
employees.first_name as "First Name",
employees.last_name as "Last Name",
employees.birth_date as "Birth Date",
salaries.salary as "Salary"
from employees , salaries
where employees.emp_no like '2667_'
and employees.emp_no = salaries.emp_no
limit 500; """

# query 3
s3 = """ select birth_date , count(*)
from employees
group by 1 
order by 2 desc
limit 10; """

# cada a variavel header irá guardar os nomes de todas as colunas do respetivo query
header1 = ['Name', 'Birthday Date', 'Employee no.', 'Job', 'Salary']
header2 = ['Employee no.', 'First Name', 'Last Name', 'Birthday Date', 'Salary']
header3 = ['Birthday Date', 'Count(*)']


# a variavel result1 irá guardar o resultado da função connectionDB, a ser executa no myMariaDB.py
result1 = connectionDB()
print ( result1 )

# se a conexão com a BD for estabelecida com sucesso (isto é, se não se verificarem erros no login)
# imprime uma linha que identifique a tabela 1
# imprime um espaço entre a linha acima e a tabela que será gerada abaixo
if result1:
    print("################# TABELA 1 - 10 EMPREGADOS COM ID 2667 + 0-9 #################")
    print(" ")
   
    # chamamos a função selecttable que recebe como parâmetros a query1 e os títulos das colunas desta query 
    result2 = selecttable(s1, header1)
    print(" ") 
    
    print("########### TABELA 2 - SALARIOS DOS 10 EMPREGADOS COM ID 2667 + 0-9 ###########")
    print(" ")
    selecttable(s2, header2)
    print(" ")
    
    print("############ TABELA 3 - Nº EMPREGADOS QUE FAZEM ANOS NA MESMA DATA ############")
    print(" ")
    selecttable(s3, header3)
    print(" ")


    # uma vez que este print está dentro do scope do result1, apenas será dado print se o result1 for true
    # caso o result2 seja impresso, chamamos a função para nos desconectarmos da BD 
    print( result2 )
    if result2: 
        disconnectionDB()
        print(disconnectionDB())