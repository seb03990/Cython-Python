import time
import py_orbita
import cy_orbita

"""Se usaron datos de wikipedia para la creacion del planeta tierra"""

#Para cada simulacion el numero de pasaos va a ser igual al tiempo, por lo que solo se creara una lista para las 2 variables
tiempo = [10000,100000,1000000,5000000,10000000]

#Se crea un formato para la impresion sobre el fichero
formato_datos = "{},{},{},{},{}\n"

with open("tierra.csv","a") as archivo:
		archivo.write("Time_span,N_setps,Python,Cython,Aceleracion\n")

for j in range(len(tiempo)):	
	
	prom_py = 0
	prom_cy = 0
	
	for i in range(30):

		inicioPy = time.time()
		
		#en python

		tierraPy = py_orbita.Planet()

		tierraPy.x = 100*10**3
		tierraPy.y = 300*10**3
		tierraPy.z = 700*10**3
		
		tierraPy.vx = 2.000*10**3
		tierraPy.vy = 29.87*10**3
		tierraPy.vz = 0.034*10**3

		tierraPy.m = 5.9741*10**24
		
		#datos de entrada (objeto plantea, tiempo, numero de pasos)
		tierraPy.step_time(tierraPy,tiempo[j],tiempo[j])
		total_py = time.time() - inicioPy
		
		inicioCy= time.time()
		
		#en cython

		tierraCy = cy_orbita.Planet()

		tierraCy.x = 100*10**3
		tierraCy.y = 300*10**3
		tierraCy.z = 700*10**3

		tierraCy.vx = 2.000*10**3
		tierraCy.vy = 29.87*10**3
		tierraCy.vz = 0.034*10**3

		tierraCy.m = 5.9741*10**24
		
		#datos de entrada (objeto plantea, tiempo, numero de pasos)
		tierraCy.step_time(tierraCy,tiempo[j],tiempo[j])
		total_cy = time.time() - inicioCy
		
		prom_py += total_py
		prom_cy += total_cy
		
	with open("tierra.csv","a") as archivo:
		archivo.write(formato_datos.format(tiempo[j],tiempo[j],prom_py,prom_cy,(prom_py/prom_cy)))
	

