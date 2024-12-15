import turtle
import time

class Forma():
    def __init__(self, nome, cor, x, y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
        
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.fillcolor(self.cor)
        self.desenhar_forma(t)
        t.end_fill()

    def desenhar_forma(self, t: turtle.Turtle):
        raise Exception('Metodo Alternativo')

class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retangulo', cor, x, y)
        self.largura = largura
        self.altura = altura

    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)
        t.end_fill()

class Triangulo(Forma):
    def __init__(self, lado, cor, x, y):
        super().__init__('Triangulo', cor, x, y)
        self.lado = lado

    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        for _ in range(3):
            t.forward(self.lado)
            t.right(120)
        t.end_fill()

class Circulo(Forma):
    def __init__(self, raio, cor, x, y):
        super().__init__('Circulo', cor, x, y)
        self.raio = raio

    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        t.circle(self.raio)
        t.end_fill()

class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y):
        super().__init__('Estrela', cor, x, y)
        self.tamanho = tamanho

    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(5):
            t.forward(self.tamanho)
            t.right(144)  


t = turtle.Turtle()
turtle.bgcolor('darkblue')

grama = Retangulo(800, 400, 'green', -400, -300)  
tronco = Retangulo(50, 150, 'brown', -25, -150) 
folhas = Circulo(50, 'green', 0, -160)  
lua = Circulo(50, 'lightyellow', 200, 100) 
estrela1 = Estrela(30, 'black', -150, 150)  
estrela2 = Estrela(20, 'black', 100, 200)  
estrela3 = Estrela(10, 'black', 150, 100)

formas = [grama, tronco, folhas, lua, estrela1, estrela2, estrela3]

for f in formas:
    f.desenhar()
    time.sleep(1)
time.sleep(3)
turtle.done()
