from Salario import Salario
from Empregado import Empregado

salario = Salario(10000, 700)
emp = Empregado("Kyle", 18, salario)
print(emp.salario_total());