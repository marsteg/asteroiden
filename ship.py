from circleshape import *
from constants import *
from asteroid import *
import random

class Ship(CircleShape):
    _id_counter = 1
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.id = Ship._id_counter
        Ship._id_counter += 1
        self.initialized = False

    def initialize(self):
        self.initialized = True

    containers = []      

    def draw(self, screen):
        #pygame.draw.circle(screen, (100, 100, 255), self.position, self.radius, 2)
        pygame.draw.polygon(screen, (100, 133, 100), self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

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
        print("Ship", self.id," killed on position: ", self.position)
        pygame.sprite.Sprite.kill(self) 


