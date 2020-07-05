import pygame

pygame.font.init()
time_delay = 50
background = (255, 255, 255)


class Board:
    def __init__(self, init_val, win):
        """
        :param init_val: initial numbers for gird board
        :param win: window
        """
        self.grid = init_val
        self.win = win
        self.width, self.height = win.get_size()
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
        _next = self.next_empty()
        if _next is not None:
            x, y = _next
        else:
            return True
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
            self.paint(True)
            pygame.time.delay(time_delay)

            if self.solve():
                return True
            self.grid[x][y] = 0
        # failed to find solution with previous moves, go back

        self.win.fill(background)
        self.paint(False)
        self.paint_box(x, y, (255, 0, 0))
        pygame.display.update()
        pygame.time.delay(time_delay)
        return False

    def paint(self, update=False):
        if update:
            self.win.fill(background)
        # first paint individual grids
        width = self.width // 9
        height = self.height // 9
        for j in range(9):
            y = j * height
            for i in range(9):
                x = i * width
                print(x, y)
                pygame.draw.lines(self.win, (0, 0, 0), True,
                                  [(x, y), (x + width, y), (x + width, y + height), (x, y + height)], 1)
        # then paint the 3X3 grid lines
        pygame.draw.line(self.win, (0, 0, 0), (width * 3, 0), (width * 3, height * 9), 4)
        pygame.draw.line(self.win, (0, 0, 0), (width * 6, 0), (width * 6, height * 9), 4)
        pygame.draw.line(self.win, (0, 0, 0), (0, height * 3), (width * 9, height * 3), 4)
        pygame.draw.line(self.win, (0, 0, 0), (0, height * 6), (width * 9, height * 6), 4)

        # paint numbers

        def paint_text(word: str, x: int, y: int, color=(0, 0, 0)):
            """
            display text on board
            :param color: color of text
            :param word: string to be displayed
            :param x: which column word is in
            :param y: which row word is in
            """
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render(word, False, color)
            text_pos = (x * width + width // 2 - textsurface.get_width() // 2, y * height + height // 2 -
                        textsurface.get_height() // 2)
            self.win.blit(textsurface, text_pos)

        for j in range(len(self.grid)):
            for i in range(len(self.grid[0])):
                if self.grid[i][j] != 0:
                    paint_text(str(self.grid[i][j]), i, j)
        if update:
            pygame.display.update()

    def paint_box(self, x, y, color):
        if type(x) is not int or type(y) is not int:
            print(type(x), type(y))
            quit()
        width = self.width // 9
        height = self.height // 9
        start_cord = (x * width, y * height)
        pygame.draw.lines(self.win, color, True, (
            start_cord,
            (start_cord[0] + width, start_cord[1]),
            (start_cord[0] + width, start_cord[1] + height),
            (start_cord[0], start_cord[1] + height)
        ))


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    frame_size = pygame.display.get_surface().get_size()
    pygame.display.set_caption("first game")
    run = True
    init_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    b = Board(init_board, win)
    while run:
        keys = pygame.key.get_pressed()
        win.fill(background)
        if keys[pygame.K_ESCAPE]:
            run = False
            print('changed run status')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                b.solve()
        b.paint()
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
