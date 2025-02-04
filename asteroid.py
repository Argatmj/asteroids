from circleshape import * 
from constants import * 
import random

class asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",center=self.position,radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astr1 = asteroid(self.position[0]+2, self.position[1]+2,new_radius)
            astr1.velocity = vec1 * 1.2
            astr2 = asteroid(self.position[0]-2, self.position[1]-2,new_radius)
            astr2.velocity = vec2 * 1.2 
