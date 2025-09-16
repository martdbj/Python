// Programa para una tienda online que durante el mes de septiembre ofrece un descuento del 15 MOD 
// Nos pedirá el mes (con letras)  y el precio y calculará el precio final
Proceso sin_titulo
	Definir mes Como Caracter;
	Escribir 'Introduzca el mes acutal';
	Leer mes;
	Definir precio Como Real;
	Escribir 'Introduzca el precio del producto';
	Leer precio;
	Si mes='septiembre' Entonces
		Escribir 'Precio con descuento: ', precio - (precio*0.15);
	SiNo
		Escribir 'Precio sin descuento: ', precio;
	FinSi
FinProceso
