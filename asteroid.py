import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_rotation = random.uniform(20, 50)        
        velocity1 = self.velocity.rotate(random_rotation)
        velocity2 = self.velocity.rotate(-random_rotation)
        radius_asteroid1 = self.radius - ASTEROID_MIN_RADIUS
        radius_asteroid2 = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius_asteroid1)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius_asteroid2)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
