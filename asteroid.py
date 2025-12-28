import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity1 = self.velocity.rotate(angle) * 1.2
        new_velocity2 = self.velocity.rotate(-angle) * 1.2
        split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid1.velocity = new_velocity1
        split_asteroid2.velocity = new_velocity2
        log_event("asteroid_split")
            
    
