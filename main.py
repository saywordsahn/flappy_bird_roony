import pgzrun

HEIGHT = 708
WIDTH = 400

gravity = 0.3
gap = 150
bird = Actor('bird1', (50, 200))
bird.speed = 1
bird.is_alive = True

top = Actor('top', (300, 0))
top.speed = 1
bottom = Actor('bottom', (300, 500 + gap))
bottom.speed = 1



def draw():
    screen.blit('background', (0, 0))
    bird.draw()
    top.draw()
    bottom.draw()



def update():
    bird.speed += gravity
    bird.y += bird.speed
    top.x -= top.speed
    bottom.x -= bottom.speed

    # reset pipes
    if top.x < 0:
        top.x = WIDTH
        bottom.x = WIDTH

    # collision
    if bird.colliderect(top) or bird.colliderect(bottom):
        bird.image = 'birddead'
        bird.is_alive = False


    # reset the bird
    if bird.y > HEIGHT:
        bird.pos = (50, 200)
        top.pos = (300, 0)
        bottom.pos = (300, 500 + gap)
        bird.speed = 1
        bird.is_alive = True
        bird.image = 'bird1'



def on_mouse_down():
    # if the bird is alive change it's speed
    if bird.is_alive:
        bird.speed = -6.5




pgzrun.go()