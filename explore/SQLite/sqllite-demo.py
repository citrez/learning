# INSERT, SELECT, UPDATE and DELETE
# This is everything you need to do in databases

# we have employees and we want to create update and delete
# employees from our database as well as being able to grab info
import sqlite3


conn = sqlite3.connect('employee.db') # the create method makes the file if it doesnt exists,
# if it does exist, it just connects

# we could do this, which just saves the table in memory
# this is useful for testings as it starts fresh each time
# conn = sqlite3.connect(':memory:') 


# lets create a cursor
c = conn.cursor()

#Creatae a TABLE

# c.execute("""CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer

# ) """)

# conn.commit()

c.execute("""INSERT INTO employees VALUES ('Ezra', 'Citron', '65000')
 """)

# c.execute("SELECT * FROM employees WHERE last = 'Citron' ")
# print(c.fetchone()) # returns a tuple
# c.execute("SELECT * FROM employees WHERE last = 'Citron' ")
# print(c.fetchall()) # returns a list of tuple(s)



### Now usings a class

from employee import Employee

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

print(emp_2.pay)
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay))

c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", 
{'first': emp_2.first,
'last':emp_2.last,
'pay': emp_2.pay}
)

c.execute("SELECT * FROM employees WHERE last = :last", {'last':'Doe'})
print(c.fetchall())



# Now a more pythonic way to
# INSERT, SELECT, UPDATE and DELETE values 
# from our DB

def insert_emp(emp):
    with conn: #so we dont need to write c.commit()
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", 
        {'first': emp.first,
        'last':emp.last,
        'pay': emp.pay})

def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last':'Doe'})
    return c.fetchall()

def get_all_emps():
    c.execute("SELECT * FROM employees")
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_3 = Employee('Yonah','Citron',0)
emp_4 = Employee('Sarah','Joffe',18000)

insert_emp(emp_3)
insert_emp(emp_4)

emps = get_emp_by_name('Citron')
print(emps)

update_pay(emp_4,30000)

all_emps = get_all_emps()
print(all_emps)

conn.close()