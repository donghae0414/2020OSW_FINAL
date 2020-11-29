from bangtal import Object

class Enemy(Object):
	def __init__(self, scene, x, y, x_size, y_size, velocity, image):
		super().__init__(image)
		self.image = image
		self.scene = scene

		self.x = x
		self.y = y
		self.x_size = x_size
		self.y_size = y_size

		self.velocity = velocity