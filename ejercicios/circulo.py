class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular(self):
        PI=3.1416
        self.area=PI*(radio*radio)
        self.perimetro =2*radio*PI

    def get_perimetro(self):
        return self.perimetro

    def get_area(self):
        return self.area

print("Ingrese el radio del circulo:  ")
radio=float(input())

circulo = Circulo(radio)
circulo.calcular()
perimetro = circulo.get_perimetro()
print(perimetro)
area = circulo.get_area()
print(area)
