# Classe empregado
class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario #Agregação

    def salario_total(self):
        return self.salario_agregado.salario_anual();