from math import sqrt

class Planet(object):
	
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
		
	def single_step(self, planet, float dt):
		
		cdef float distance = sqrt(planet.x**2 + planet.y**2  + planet.z**2)
		
		cdef float Fx = -planet.x / distance**3
		cdef float Fy = -planet.y / distance**3
		cdef float Fz = -planet.z / distance**3
		
		planet.vx += dt * Fx / planet.m
		planet.vy += dt * Fy / planet.m
		planet.vz += dt * Fz / planet.m
		
	def step_time(self, planet, int time_span,int n_steps):
		
		cdef float dt = 0.0
		cdef int j
		
		dt = time_span / n_steps
		
		for j in range(n_steps):
			self.single_step(planet,dt)
