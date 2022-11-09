# Comparativa de rendimiento Cython vs Python

Bienvenido usuario.

Este repositorio cuenta con 2 algoritmos que solucionan el mismo ejercicio (Problema planeta en orbita), sin embargo, aunque los 2 algoritmos cumplen la misma funcion, el lenguaje en el que estan diseñados es diferente, un algoritmo usa python y el otro cython. El proposito de estos 2 algoritmos es compararlos y discutir acerca del tiempo de ejecucion para cada uno de ellos. Si deseas realizar la ejecucion desde tu computador realiza los siguientes pasos:

1) Descargar los archivos del repositorio
2) Ejecutar el Makefile desde la terminal con el comando 'make all'
3) Ejecutar el archivo prueba.py desde la terminal con el comando 'python3 prueba.py'
4) Abrir el archivo .csv que genera el punto 3 y analisar los reultados obtenidos

Contenido del repositorio:

* Makefile (Elimina los archivos *.so *.c *pyc de existir y ejecuta automaticamente el setup)
* setup.py (Necesario para importar el programa de cython)
* prueba.py (Ejecuta calcula los tiempos)
* py_orbita.py (algoritmo en python)
* cy_orita.pyx (algoritmo en cython)
* Cython vs Python (PDF)

Notas:

* Los algoritmos py_orbita.py y cy_orbita.pyx necesitan 2 datos de entrada time_steps y n_steps
* prueba.py es un algoritmo elaborado en python, este contiene un conjunto de elementos que seran los datos de entrada para los algoritmos, asi que si       deseas realizar el experimento con otros datos debes cambiar el conjunto de elementos.
* Importante realizar el Makefile, de lo contrario prueba.py no reconocera el algoritmo cy_orbita.pyx, por lo que no se podra realizar el analisis
* Para mas informacion consulte el pdf
