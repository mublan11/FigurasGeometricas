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


        self.lado = 4
        self.baseRectangulo = 10
        self.hRectangulo = 9
        self.radio = 3 
        self.ladoA = 11
        self.ladoB = 05
        self.ladoH = 15

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