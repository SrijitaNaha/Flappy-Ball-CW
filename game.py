import pgzrun
from random import randint

# Constants
TITLE = 'Flappy Ball'
WIDTH, HEIGHT = 800, 600
GRAVITY = 2000.0  # pixels per second per second
BALL_RADIUS = 40

# Colors
CLR = (randint(0, 255), randint(0, 255), randint(0, 255))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.radius = BALL_RADIUS

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, CLR)

    def update(self, dt):
        # Apply constant acceleration formulae
        uy = self.vy
        self.vy += GRAVITY * dt
        self.y += (uy + self.vy) * 0.5 * dt

        # detect and handle bounce
        if self.y > HEIGHT - self.radius:  # we've bounced!
            self.y = HEIGHT - self.radius  # fix the position
            self.vy = -self.vy * 0.9  # inelastic collision

        # X component doesn't have acceleration
        self.x += self.vx * dt
        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx

def draw():
    screen.clear()
    ball.draw()

def update(dt):
    ball.update(dt)

def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    if key == keys.SPACE:
        ball.vy = -500

ball = Ball(50, 100)

pgzrun.go()