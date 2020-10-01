import pygame

# import time

pygame.init()

screen_width_x = 500
screen_width_y = 480

win = pygame.display.set_mode((screen_width_x, screen_width_y))  # This is the window that we draw on
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('./images/R1.png'), pygame.image.load('./images/R2.png'),
             pygame.image.load('./images/R3.png'), pygame.image.load('./images/R4.png'),
             pygame.image.load('./images/R5.png'), pygame.image.load('./images/R6.png'),
             pygame.image.load('./images/R7.png'), pygame.image.load('./images/R8.png'),
             pygame.image.load('./images/R9.png')]
walkLeft = [pygame.image.load('./images/L1.png'), pygame.image.load('./images/L2.png'),
            pygame.image.load('./images/L3.png'), pygame.image.load('./images/L4.png'),
            pygame.image.load('./images/L5.png'), pygame.image.load('./images/L6.png'),
            pygame.image.load('./images/L7.png'), pygame.image.load('./images/L8.png'),
            pygame.image.load('./images/L9.png')]
bg = pygame.image.load('./images/bg.jpg')
char = pygame.image.load('./images/standing.png')

clock = pygame.time.Clock()
game_speed = 27

red_coordinate = 255
green_coordinate = 0
blue_coordinate = 0


class player():
    """ pass """
    def __init__(self, x, y, width, height):
        self.x = x  # position
        self.y = y  # position

        self.width = width  # hit box
        self.height = height  # hit box
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.previous_position = None
        self.walk_count = 0
        self.standing = True

    def draw(self, window):
        """ pass """
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walk_count // 3], (self.x, self.y))  # draws images
                self.walk_count += 1  # cycle through the loop to give the illusion of movement
            elif self.right:
                window.blit(walkRight[self.walk_count // 3], (self.x, main_player.y))
                self.walk_count += 1
        else:
            # window.blit(char, (self.x, self.y))
            if self.is_jump:
                window.blit(char, (self.x, self.y))
                # print("jump")
            elif not self.right and self.left:
                # print("left")
                window.blit(walkLeft[0], (self.x, self.y))
                self.previous_position = "LEFT"
            elif self.right and not self.left:
                # print("right")
                window.blit(walkRight[0], (self.x, self.y))
                self.previous_position = "RIGHT"
            else:
                if self.previous_position is None:
                    # print("None")
                    window.blit(char, (self.x, self.y))
                elif self.previous_position == "RIGHT":
                    window.blit(walkRight[0], (self.x, self.y))
                    self.previous_position = "RIGHT"
                elif self.previous_position == "LEFT":
                    window.blit(walkLeft[0], (self.x, self.y))
                    self.previous_position = "LEFT"
                else:
                    # print("pass")
                    pass


class projectile():
    """ pass """
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


# initial draw
def redrawGameWindow():
    win.blit(bg, (0, 0))
    main_player.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
main_player = player(300, 410, 64, 64)
bullets = []
run = True
while run:
    # pygame.time.delay(game_speed)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if main_player.previous_position == "LEFT":
            facing = -1
        elif main_player.previous_position == "RIGHT":
            facing = 1
        else:
            pass

        if len(bullets) < 5:
            bullets.append(projectile(round(main_player.x + main_player.width // 2),
                                      round(main_player.y + main_player.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and main_player.x > main_player.vel:
        # color_changer('LEFT')
        main_player.left = True
        main_player.right = False
        main_player.standing = False
        main_player.x -= main_player.vel

    elif keys[pygame.K_RIGHT] and main_player.x < screen_width_x - main_player.width - main_player.vel:
        # color_changer('RIGHT')
        main_player.left = False
        main_player.right = True
        main_player.standing = False
        main_player.x += main_player.vel

    else:
        main_player.standing = True
        main_player.walk_count = 0

    if not main_player.is_jump:
        if keys[pygame.K_UP]:
            main_player.is_jump = True
            main_player.left = False
            main_player.right = False
            main_player.walk_count = 0
    else:
        if main_player.jump_count >= -10:
            neg = 1
            if main_player.jump_count < 0:
                neg = -1
            main_player.y -= (main_player.jump_count ** 2) * 0.5 * neg
            main_player.jump_count -= 1
        else:
            main_player.is_jump = False
            main_player.jump_count = 10

    redrawGameWindow()

pygame.quit()
