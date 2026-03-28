import pygame,random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        as_1_vel = self.velocity.rotate(angle)
        as_2_vel = self.velocity.rotate(angle * -1)
        self.radius -= ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x,self.position.y,self.radius)
        new_asteroid_2 = Asteroid(self.position.x,self.position.y,self.radius)
        new_asteroid_1.velocity = as_1_vel * 1.2
        new_asteroid_2.velocity = as_2_vel * 1.2
