import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)

    running = True
    drawing = False
    clock = pygame.time.Clock()
    x, y = 0, 0
    vx, vy = 100, 100
    r = 10
    t = 0
    circle = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Боремся с пограничным залипанием
                x = x if x >= r else r
                x = x if x <= width - r else width - r
                y = y if y >= r else r
                y = y if y <= height - r else height - r
                circle.append([x, y, vx, vy])

        screen.fill((0, 0, 0))

        for c in circle:
            if c[1] <= r:
                c[3] = -c[3]
            if c[0] >= width - r:
                c[2] = -c[2]
            if c[0] <= r:
                c[2] = -c[2]
            if c[1] >= height - r:
                c[3] = -c[3]
            c[0] -= c[2] * t
            c[1] -= c[3] * t
            pygame.draw.circle(screen, pygame.Color('white'), (int(c[0]), int(c[1])), r)

        t = clock.tick() / 1000
        pygame.display.flip()
    pygame.quit()
