# -*- coding: utf-8 -*-

"""
    Autor: Diego Misael Blanco Murillo.
    Fecha: 01/OCT/17
"""

from lettuce import step, world
from figuras import Figuras

#Figuras Geometricas

@step(u'cuando realizo la operacion entonces')
def cuando_realizo_la_operacion_entonces(step):
    pass

@step(u'Dado que introduzco el numero "([^"]*)" cuadrado')
def dado_que_introduzco_el_numero_group1_cuadrado(step, num):
    world.figura = Figuras()
    world.figura.areaCuadrado(int(num))

@step(u'obtengo un resultado de "([^"]*)"')
def obtengo_un_resultado_de_group1(step, esperado):
    obtenido = world.figura.obtener_resultado()
    a = 'El resultado esperado es '
    b = ' y el obtenido es '
    assert str(esperado) == str(obtenido), str(a) + 
                            str(esperado) + str(b) + 
                            str(obtenido)

@step(u'Dado que introduzco el numero "([^"]*)" y "([^"]*)" rectangulo')
def dado_que_introduzco_el_numero_group1_y_group2_rectangulo(step, num1, num2):
    world.figura = Figuras()
    world.figura.areaRectangulo(int(num1), int(num2))

@step(u'Dado que introduzco el radio de "([^"]*)"')
def dado_que_introduzco_el_radio_de_group1(step, num):
    world.figura = Figuras()
    world.figura.areaCirculo(num)

@step(u'Dado que introduzco los numeros "([^"]*)", "([^"]*)", "([^"]*)"')
def dado_que_introduzco_los_numeros_group1_group2_group3(step, num1, num2, num3):
    world.figura = Figuras()
    world.figura.areaTrapecio(int(num1), int(num2), int(num3))