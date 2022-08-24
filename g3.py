import pgzrun

HEIGHT = 500
WIDTH = 500

images = Actor('images', pos=(200,200))

def draw():
    screen.fill('white')
    images.draw()

def update():
    images.y += 1
    if images.y > HEIGHT:
        images.Y = 0

pgzrun.go()        