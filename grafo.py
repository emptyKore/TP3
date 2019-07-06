import random

class Grafo:
	"""Representación del TAD Grafo"""

	def __init__(self):
		"""Crea una grafo vacío."""
		self.grafo = {}
		self.cantidad = 0

	def cantidad_vertices(self):
		"""Devuelve la cantidad de vertices en ell grafo."""
		return self.cantidad

	def agregar_vertice(self, vertice):
		"""Agrega un vertice al grafo."""
		self.grafo[vertice] = {}
		self.cantidad += 1


	def borrar_vertice(self, vertice):
		"""Borra un vertice del grafo."""
		if vertice not in self.grafo:
			return None

		for clave in self.grafo:

			if vertice in self.grafo[clave]:
				self.grafo[clave].pop(vertice)

		self.cantidad -= 1
		return self.grafo.pop(vertice)


	def agregar_arista(self, vertice_1, vertice_2, peso = 0):
		"""Agrega una arista entre dos vertices."""
		self.grafo[vertice_1][vertice_2] = peso
		

	def borrar_arista(self, vertice_1, vertice_2):
		"""Borra una arista entre dos vertices."""

		if vertice_2 not in self.grafo[vertice_1]:
			return None

		return self.grafo[vertice_1].pop(vertice_2)

	def vertices_conectados(self, vertice_1, vertice_2):
		"""Devuelve si dos vertices estan conectados."""
		return vertice_2 in self.grafo[vertice_1]


	def vertice_random(self):
		"""Devuelve un vertice al azar del grafo."""
		return random.choice(list(self.grafo.keys()))


	def vertices(self):
		"""Obtiene todos los vertices del grafo."""
		return self.grafo.keys()


	def adyacentes(self, vertice):
		"""Obtiene todos los adyacentes a un vertice."""
		return self.grafo[vertice].keys()


	def __iter__(self):
		"""Devuelve un iterador sobre los vertices."""
		return iter(self.grafo)


	def __str__(self):
		cadena = ""
		for v in self.grafo.keys():
			cadena += v + ": "
			for w in self.grafo[v].keys():
				cadena += w + " "
			cadena += "\n"
		return cadena


