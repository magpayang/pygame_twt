import pygame
# import time

pygame.init()

screen_width_x = 500
screen_width_y = 500

win = pygame.display.set_mode((screen_width_x, screen_width_y))  # This is the window that we draw on
pygame.display.set_caption("First Game")

red_coordinate = 255
green_coordinate = 0
blue_coordinate = 0

x = 50
y = 50

width = 40
height = 60

vel = 10

is_jump = False
jump_count = 10

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        red_coordinate = 0
        green_coordinate = 255
        blue_coordinate = 0
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width_x - width - vel:
        x += vel
        red_coordinate = 0
        green_coordinate = 0
        blue_coordinate = 255
    if not is_jump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_width_y - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (red_coordinate, green_coordinate, blue_coordinate), (x, y, width, height))
    pygame.display.update()

pygame.quit()



