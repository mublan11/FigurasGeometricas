class Areas():
    def __init__(self):
        self.pi = 3.1416
        
    def areaCuadrado(self, lado):
        return lado * lado

    def areaRectangulo(self, base, altura):
        return base * altura    

    def areaCirculo(self, radio):   
        return (self.pi ** radio)**2

    def areaTrapecio(self, a, b, h):
        return (a+b)/2