from pico2d import *
import random

# Game object class here

class grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 300), 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += 5
        self.frame = (self.frame+1)%8

class smallball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(10, 20)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y >= 50 + self.speed:
            self.y -= self.speed


class bigball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(10, 20)
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):

        if self.y >= 70 + self.speed:
            self.y -= self.speed


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = grass()
team = [boy() for i in range(11)]

ball =[]
for i in range(20):
    x = random.randint(1, 2)
    if x == 1:
        ball.append(smallball())
    else:
        ball.append(bigball())

running = True
# game main loop code

while running:
    handle_events()

    #gamle logic

    #game drawing
    clear_canvas()
    grass.draw()

    for ball_1 in ball:
        ball_1.draw()
    for ball_1 in ball:
        ball_1.update()
    for boy in team:
        boy.draw()
    for boy in team:
        boy.update()

#    boy.update()
    update_canvas()


    delay(0.02)
# finalization code