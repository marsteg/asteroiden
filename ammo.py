from circleshape import *
from constants import *
from asteroid import *
import random

class Ammo(CircleShape):
    _id_counter = 1
    def __init__(self, x, y):
        self.radius = 10
        super().__init__(x, y, self.radius)
        self.rotation = 0
        self.id = Ammo._id_counter
        Ammo._id_counter += 1


    containers = []      

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius/2)
        asteroid1.velocity = velocity1 * 1.2
        asteroid1.initialize()
        asteroid2 = Asteroid(self.position.x, self.position.y, radius/2)
        asteroid2.velocity = velocity2 * 1.2
        asteroid2.initialize()

    def kill(self):
        print("Ammo collected", self.id," on position: ", self.position)
        pygame.sprite.Sprite.kill(self) 


