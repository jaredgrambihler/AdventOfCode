import numpy as np

with open("input/day4input.txt") as f:
    input_text = f.read()

input_lines = input_text.strip().splitlines()

called_numbers = [int(x) for x in input_lines[0].split(",")]


class Board:
    _board: list[list[int]]
    _marked: list[list[bool]]
    _num_to_index: dict[int, tuple[int, int]]

    def __init__(self, board):
        self._board = board
        self._marked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self._num_to_index = dict()
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                self._num_to_index[self._board[i][j]] = (i, j)

    def mark(self, val: int) -> bool:
        if val in self._num_to_index:
            i, j = self._num_to_index[val]
            self._marked[i][j] = True
        return self.check_win()
    
    def check_win(self) -> bool:
        # row wins
        for row in self._marked:
            if all(row):
                return True
        marked_np = np.array(self._marked)
        for i in range(len(marked_np[0])):
            if all(marked_np[:, i]):
                return True
        # check diagonal
        top_left_to_right_diag = True
        top_right_to_left_diag = True
        for i in range(len(self._marked)):
            if self._marked[i][i] == False:
                top_left_to_right_diag = False
            if self._marked[i][-i-1] == False:
                top_right_to_left_diag = False
        return top_left_to_right_diag or top_right_to_left_diag

    def unmarked_sum(self) -> int:
        unmarked_sum = 0
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if not self._marked[i][j]:
                    unmarked_sum += self._board[i][j]
        return unmarked_sum


def get_boards(board_lines) -> list[Board]:
    boards = []
    current_board = []
    for line in board_lines:
        line = line.strip()
        if line == "":
            boards.append(current_board)
            current_board = []
        else:
            current_board.append([int(x) for x in line.split()])
    return [Board(board) for board in boards]


def get_winning_score(called_numbers, boards):
    for num in called_numbers:
        for board in boards:
            win = board.mark(num)
            if win:
                score = board.unmarked_sum() * num
                return score
    return -1


def get_last_winning_board_score(called_numbers, boards):
    boards = set(boards)
    for num in called_numbers:
        to_remove = []
        for board in boards:
            win = board.mark(num)
            if win and len(boards) > 1:
                to_remove.append(board)
            elif win and len(boards) == 1:
                return board.unmarked_sum() * num
        for board in to_remove:
            boards.remove(board)
    return -1

boards = get_boards(input_lines[2:])

print("Part 1")
print(f"Winning score: {get_winning_score(called_numbers, boards)}")
print("Part 2")
print(f"Last winning score: {get_last_winning_board_score(called_numbers, boards)}")

