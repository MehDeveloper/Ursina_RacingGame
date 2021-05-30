from ursina import *
app = Ursina()

class Car(Entity):
	def __init__(self):
		super().__init__()
		self.model = 'quad'
		self.scale = Vec2(.5,.5)
		self.color = color.rgb(50,50,100)

		self.speed = 5
		self.turn_speed = 2
		self.velocity = Vec3(0,0,0)

	def update(self):
		self.forward_rc = raycast(self.world_position, direction=self.up, distance=.5, debug=True)
		self.reverse_rc = raycast(self.world_position, direction=self.down, distance=.5, debug=False)

		if held_keys['w'] and not self.forward_rc.hit:
			self.velocity += self.up*time.dt*self.speed

		if self.forward_rc.hit:
			self.velocity = Vec3(0,0,0)

		if held_keys['s'] and not self.reverse_rc.hit:
			self.velocity += self.down*time.dt*self.speed

		if self.reverse_rc.hit and not held_keys['w']:
			self.velocity = Vec3(0,0,0)

		self.position += self.velocity/10
		self.rotation += Vec3(0,0,(held_keys['d']-held_keys['a'])*self.turn_speed)
		self.velocity -= self.velocity/15

if __name__ == '__main__':
	car = Car()

	square = Entity(model='quad', collider='box', position = Vec2(3,3))

	def update():
		camera.x, camera.y = car.x, car.y

	app.run()