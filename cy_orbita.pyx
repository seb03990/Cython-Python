#cython: language_level=3

cimport cython

cdef extern from "math.h":
	double sqrt(double x) nogil
	
"""from math import sqrt"""

cdef class Planet(object):
	
	cdef public double x,y,z,vx,vy,vz,m
		
	def __init__(self):
			
		#posicion y velocidad inicial
		self.x = 1.0
		self.y = 0.0
		self.z = 0.0
		self.vx = 0.0
		self.vy = 0.5
		self.vz = 0.0
			
		#masa
		self.m = 1.0
			
	"""¿Que pasa si distance = 0?
	Se usara un decorador de cython para evitar la divicion por 0 y evitar el costo
	computacional"""
	
	@cython.cdivision(True)	
	cdef void single_step(self,Planet planet, float dt) nogil:
			
		cdef double distance,Fx,Fy,Fz
		distance = sqrt(planet.x**2+planet.y**2+planet.z**2)
		Fx = -planet.x/distance**3
		Fy = -planet.y/distance**3
		Fz = -planet.z/distance**3
		planet.vx += dt * Fx/planet.m
		planet.vy += dt * Fy/planet.m
		planet.vz += dt * Fz/planet.m
				
	def step_time(self,Planet planet, float time_span,int n_steps):
			
		cdef float dt 
		cdef int j
		dt = time_span/n_steps
			
		"""Habilitar la posibilidad de paralelismo"""
		with nogil:
			for j in range(n_steps):
				self.single_step(planet,dt)
