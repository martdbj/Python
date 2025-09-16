// Programa que presenta un menú y que al pulsar un número musetra una recomendación de cada tipo
Proceso menu
	Definir eleccion Como Real;
	Escribir '1-Literatura';
	Escribir '2-Cine';
	Escribir '3-Música';
	Escribir '4-Videojuegos';
	Escribir '5-Salir';
	Escribir 'Elige lo que prefieras';
	Leer eleccion;
	Segun eleccion  Hacer
		1:
			Escribir 'El guardian entre el centeno';
		2:
			Escribir 'Pulp Fiction';
		3:
			Escribir 'BTS';
		4:
			Escribir 'Mario Galaxy';
		De Otro Modo:
			Escribir 'Has salido del programa';
	FinSegun
FinProceso
