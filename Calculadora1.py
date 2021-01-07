#funcao retorna valor metodo não no python não tem deferença explicita utilizamos apenas comando def declara metodo
class Calculadora1:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    def soma (self):
        return self.a + self.b
    def subtra(self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def divisao(self):
        return self.a / self.b

if __name__ == '__main__':

    calculadora = Calculadora1(10, 2)
    print(calculadora.a)
    print(calculadora.soma())
    print(calculadora.subtra())
    print(calculadora.multi())
    print(calculadora.divisao())