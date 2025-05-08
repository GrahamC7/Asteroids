from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.position = position.copy()
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), tuple(map(int, self.position)), SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y