import pygame
import random
from asteroid import Asteroid
from constants import *
from ship import Ship
from ammo import *


class Moon(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-SHIP_MAX_RADIUS, y * SCREEN_HEIGHT/2),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH/2 + SHIP_MAX_RADIUS, y * SCREEN_HEIGHT/2
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH/2, -SHIP_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + SHIP_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.radius = 50
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.ammo_spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        ship = Ship(position.x, position.y, radius)
        print("spawning ship ", ship.id, " at position: ", position)
        ship.initialize()
        ship.velocity = velocity

    def ammospawn(self, position):
        randNum = random.randint(100, 200)
        ammo = Ammo(position.x+randNum, position.y+randNum)
        print("spawning ammo ", ammo.id, " at position: ", position)

    def draw(self, screen):
        pygame.draw.rect(screen, (209, 57, 202), (0, 0, SCREEN_WIDTH/2+2, SCREEN_HEIGHT/2+2), 2)
        screen.fill((211, 211, 211), (0, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self, dt):
        self.spawn_timer += dt
        self.ammo_spawn_timer += dt
        if self.ammo_spawn_timer > AMMO_SPAWN_RATE:
            self.ammo_spawn_timer = 0
            edge = random.choice(self.edges)
            position = edge[1](random.uniform(0, 1))
            self.ammospawn(position)

        if self.spawn_timer > SHIP_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(SHIP_MIN_RADIUS * kind, position, velocity)