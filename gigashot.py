from circleshape import *
from constants import *

class GigaShot(CircleShape):
    def __init__(self, x, y):
        self.radius = 30
        super().__init__(x, y, self.radius)
        self.rotation = 0

    containers = []        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        