#Fichero para la creacion del objeto compartido

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("pyx_orbita.pyx"))

setup(ext_modules = exts)
