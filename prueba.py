import time
import py_orbita
import cy_orbita

"""Con datos de wikipedia"""

#en python

tierraPy = py_orbita.Planet()

tierraPy.x = 100*10**3
tierraPy.y = 300*10**3
tierraPy.z = 700*10**3

tierraPy.vx = 2.000*10**3
tierraPy.vy = 29.87*10**3
tierraPy.vz = 0.034*10**3

tierraPy.m = 5.9741*10**24

#en cython

tierraCy = cy_orbita.Planet()

tierraCy.x = 100*10**3
tierraCy.y = 300*10**3
tierraCy.z = 700*10**3

tierraCy.vx = 2.000*10**3
tierraCy.vy = 29.87*10**3
tierraCy.vz = 0.034*10**3

tierraCy.m = 5.9741*10**24

time_span = 400
n_steps = 2000000

#Se crea un formato para la impresion sobre el fichero
formato_datos = "{},{}\n"

for i in range(3):

	inicioPy = time.time()
	tierraPy.step_time(tierraPy,time_span,n_steps)
	total_py = time.time() - inicioPy
	
	inicioCy= time.time()
	tierraCy.step_time(tierraCy,time_span,n_steps)
	total_cy = time.time() - inicioCy
	
	with open("tierra.csv","a") as archivo:
		archivo.write(formato_datos.format(total_py,total_cy))
	

