import pygame

class Board:
    def __init__(self, width, height, win):
        # 0 represents empty
        self.grid = [[0] * 9] * 9
        self.win = win
        self.width = width
        self.height = height
        self.paint()

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

    def paint(self):
        width = self.width // 9
        height = self.width // 9
        for j in range(9):
            y = j * height
            for i in range(9):
                x = i * width
                pygame.draw.lines(win, (255, 0, 0), True,
                                  [(x, y), (x + width, y), (x + width, y + height), (x, y + height)], 2)


background = (255, 255, 255)
pygame.init()
win = pygame.display.set_mode((800, 800))
frame_size = pygame.display.get_surface().get_size()
pygame.display.set_caption("first game")
run = True
b = Board(500, 500, win)
while run:
    # pygame.time.delay()
    keys = pygame.key.get_pressed()
    win.fill(background)
    if keys[pygame.K_ESCAPE]:
        run = False
        print('changed run status')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
    b.paint()
    pygame.display.update()
pygame.quit()
