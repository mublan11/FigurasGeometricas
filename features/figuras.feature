Feature: Calcular el area de una figura geometrica
	Como usuario de la area de una figura
	deseo calcular el area de cualquier figura geometrica
	para obtener mi edad biologica

	Scenario: Area de un cuadrado
		Dado que introduzco el numero "44" cuadrado
		cuando realizo la operacion entonces
		obtengo un resultado de "1936"

	Scenario: Area de un rectangulo
		Dado que introduzco el numero "44" y "10" rectangulo
		cuando realizo la operacion entonces
		obtengo un resultado de "440"

	Scenario: Area de un circulo
		Dado que introduzco el radio de "11"
		cuando realizo la operacion entonces
		obtengo un resultado de "380"

	Scenario: Area de un trapecio
		Dado que introduzco los numeros "11", "2", "12"
		cuando realizo la operacion entonces
		obtengo un resultado de "78"