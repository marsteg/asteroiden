from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    _id_counter = 1
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.id = Asteroid._id_counter
        Asteroid._id_counter += 1
        self.initialized = False

    def initialize(self):
        self.initialized = True

    containers = []     

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

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
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid1.initialize()
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = velocity2 * 1.2
        asteroid2.initialize()

    def kill(self):
        print("Asteroid", self.id,"killed on position: ", self.position)
        pygame.sprite.Sprite.kill(self) 


