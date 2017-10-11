class SnakeMove:
    def move(self, board):
        snake = [None] * 10

        for i, line in enumerate(board):
            for j, pixel in enumerate(line):
                if pixel != '.':
                    snake[int(pixel)] = [i, j]

        max_i = len(board)
        max_j = len(board[0])

        snake_tail = -1
        for pixel in snake:
            if not pixel:
                break
            snake_tail += 1

        new_snake = snake[:]
        new_snake[0] = [snake[0][0] + snake[0][0] - snake[1][0],
                        snake[0][1] + snake[0][1] - snake[1][1]]

        if new_snake[0][0] >= max_i or new_snake[0][0] < 0:
            return ['YOU LOST']
        if new_snake[0][1] >= max_j or new_snake[0][1] < 0:
            return ['YOU LOST']

        if (board[new_snake[0][0]][new_snake[0][1]] != '.' and
                board[new_snake[0][0]][new_snake[0][1]] != str(snake_tail)):
            return ['YOU LOST']

        for i in range(1, 10):
            if new_snake[i]:
                new_snake[i] = snake[i - 1]

        new_board = [['.'] * max_j for i in range(max_i)]
        for i, pixel in enumerate(new_snake):
            if not pixel:
                break
            new_board[pixel[0]][pixel[1]] = str(i)

        for i in range(len(new_board)):
            new_board[i] = ''.join(new_board[i])
        return new_board
