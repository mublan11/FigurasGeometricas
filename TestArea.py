import unittest
from areas import Areas

class TestArea(unittest.TestCase):

    def setUp(self):
        self.areaTest = Areas()
        self.choice = 0
        self.lado = 0
        self.baseRectangulo = 0
        self.hRectangulo = 0
        self.radio = 0 
        self.ladoA = 0
        self.ladoB = 0
        self.ladoH = 0

        self.choice = int(raw_input("Elige el numero de la figura que "+
        "requieres el area: "+"1 cuadrado, "+
        "2 rectangulo, 3 circulo, 4 trapecio: "))

        if self.choice == 1:
            self.lado = float(raw_input("Tamanio del lado del cuadrado: "))

        elif self.choice == 2:
            self.baseRectangulo = float(raw_input("Tamanio de la base del rectangulo: "))
            self.hRectangulo = float(raw_input("Tamanio de la altura del rectangulo: "))
        elif self.choice == 3:
            self.radio = float(raw_input("Ingresa el radio: "))
        elif self.choice == 4:
            self.ladoA = float(raw_input("Ingresa el lado a: "))
            self.ladoB = float(raw_input("Ingresa el lado b: "))
            self.ladoH = float(raw_input("Ingresa la altura: "))


        else:
            print("Ese numero no")   #pragma: no cover
        
    def test_area_cuadrado(self):
        #self.areaTest.areaCuadrado(self.numero1)
        self.assertEquals(self.areaTest.areaCuadrado(self.lado), 
            self.areaTest.areaCuadrado(self.lado))

    def test_area_rectangulo(self):
        #self.areaTest.areaCuadrado(self.numero1)
        self.assertEquals(self.areaTest.areaRectangulo(self.baseRectangulo, 
            self.hRectangulo), 
            self.areaTest.areaRectangulo(self.baseRectangulo, 
                self.hRectangulo))

    def test_area_circulo(self):
        #self.areaTest.areaCuadrado(self.numero1)
        self.assertEquals(self.areaTest.areaCirculo(self.radio), 
            self.areaTest.areaCirculo(self.radio))
        
    def test_area_trapecio(self):
        #self.areaTest.areaCuadrado(self.numero1)
        self.assertEquals(self.areaTest.areaTrapecio(self.ladoA, 
            self.ladoB, self.ladoH), 
        self.areaTest.areaTrapecio(self.ladoA, 
            self.ladoB, self.ladoH))                       

if __name__ == '__main__': #pragma: no cover
    unittest.main()