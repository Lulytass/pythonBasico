#clase punto
class Punto():
    def  __init__(self, x, y) : # metodo contructor de la clase con el metodo especial __init__()
        self.x=x   # Al atributo nombre le asigno el nombre que recibi coomo parametro
        self.y=y 
        
    def __str__(self):
        return f"(X:{self.x}, Y:{self.y})"

        
     
class Rectangulo():
    def  __init__(self, pto1, pto2) : # metodo contructor de la clase con el metodo especial __init__()
        self.pto1 = pto1   # Al atributo nombre le asigno el nombre que recibi coomo parametro
        self.pto2 = pto2   
    def __str__(self):
        return f"{self.pto1}, {self.pto2}"
    def superficie(self):
        return abs(self.pto1.x - self.pto2.x) * abs(self.pto1.y - self.pto2.y)
    def perimetro(self):
        return 2 * abs(self.pto1.x - self.pto2.x) + 2 * abs(self.pto1.y - self.pto2.y)



#programa principal
pto1 = Punto(3,2)
print(pto1)
pto2 = Punto(-1,-2)
print(pto2)

rect1 = Rectangulo(pto1,pto2)
sup = rect1.superficie()
per = rect1.perimetro()
print(rect1)
print(f"Superficie: {sup}")
print(f"Perimetro: {per}")