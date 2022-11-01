import time
import py_orbita
import pyx_orbita

#en python
inicio = time.time()
tierra = py_orbita.Planet()
tierra.step_time(tierra,100000,100000)
fin = time.time()
total_py = fin - inicio

#en cython
inicio2 = time.time()
tierra = pyx_orbita.Planet()
tierra.step_time(tierra,100000,100000)
fin2 = time.time()
total_cy = fin2 - inicio2


print('Tiempo total en Python: ',total_py)
print('Tiempo total en Cython: ',total_cy)
print('Cython es mas rapido que python {} veces'.format(total_py/total_cy))
