import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def collides_with(self, other_shape):
        # Step 1. Calculate distance between the centers
        distance = self.position.distance_to(other_shape.position)
        # Step 2. calculate the sum of the radii
        sum_of_radii = self.radius + other_shape.radius
        # Step 3. if distance <= sum_of_radii, there is a collision
        return distance <= sum_of_radii

    def update(self, dt):
        # must override
        pass


