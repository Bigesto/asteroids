import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        random_angle = random.uniform(20, 50)
        
        split_one = self.velocity.rotate(random_angle)
        split_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = split_one * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = split_two * 1.2