import pygame

"""
background = (0, 0, 0)
pygame.init()
win = pygame.display.set_mode((500, 500))
frame_size = pygame.display.get_surface().get_size()
pygame.display.set_caption("first game")

x = 50
y = 50
width = 40
height = 60
delta = 2
jumping = False
velocity = 0

jump_force = 10
gravity = 0.2

run = True
while run:
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False



    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and 0 < x < frame_size[0] - width:
        x -= delta
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and 0 < x < frame_size[0] - width:
        x += delta
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not jumping:
        jumping = True
        velocity = jump_force

    if jumping:
        if velocity < -jump_force:
            jumping = False
            velocity = 0
        else:
            y -= velocity
            velocity -= gravity
    if any(pygame.mouse.get_pressed()):
        x, y = pygame.mouse.get_pos()
        x -= width // 2
        y -= height // 2



    win.fill(background)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
"""


class Board:
    def __init__(self, x: int, y: int):
        # 0 represents empty
        self.grid = [[0] * 9] * 9

    def next_empty(self) -> (int, int):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[x][y] == 0:
                    return x, y

    def solve(self) -> bool:
        """
        :return: true if self.grid is solved
        """
        x, y = self.next_empty()
        options = {i for i in range(1, 10)}
        for i in range(len(self.grid[0])):
            if self.grid[i][y] in options:
                options.remove(self.grid[i][y])
        for j in range(len(self.grid)):
            if self.grid[x][j] in options:
                options.remove(self.grid[x][j])
        start_x = x - x % 3
        start_y = y - y % 3
        for j in range(start_y, start_y + 3):
            for i in range(start_x, start_x + 3):
                if self.grid[i][j] in options:
                    options.remove(self.grid[i][j])
        for num in options:
            self.grid[x][y] = num
            if self.solve():
                return True
            self.grid[x][y] = 0

        return False



background = (0, 0, 0)
pygame.init()
win = pygame.display.set_mode((500, 500))
frame_size = pygame.display.get_surface().get_size()
pygame.display.set_caption("first game")
run = True
while run:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
        print('changed run status')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass

    """    
    win.fill(background)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    pygame.quit()
    """
