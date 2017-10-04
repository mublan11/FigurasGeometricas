# -*- coding: utf-8 -*-

"""
	Autor: Diego Misael Blanco Murillo.
	Fecha: 01/OCT/17
"""

import math
class Figuras():
	def __init__(self):
		self.resultado = 0
		self.pi = 3.1416
	def obtener_resultado(self):
		return int(self.resultado)
	def areaCuadrado(self, lado):
		self.resultado = lado * lado	
	def areaRectangulo(self, base, altura):
		self.resultado = base * altura	
	def areaCirculo(self, radio):	
		self.resultado = math.pow(float(radio), 2.00) * float(self.pi)
	def areaTrapecio(self, ladoA, ladoB, altura):
		self.resultado = int((float(ladoA + ladoB) / 2) * (altura))