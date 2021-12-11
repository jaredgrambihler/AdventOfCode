import copy

with open("input/day11input.txt") as f:
    input_text = f.read()

class OctoGrid:
    _grid: list[list[int]]
    _flashes: int

    def __init__(self, grid):
        self._grid = copy.deepcopy(grid)
        self._flashes = 0


    @property
    def flashes(self):
        return self._flashes


    @property
    def all_flashed(self):
        for row in self._grid:
            for x in row:
                if x != 0:
                    return False
        return True


    def step(self):
        # increase all grid values by 1
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                self._grid[i][j] += 1
        flashed = [[False for _ in range(len(self._grid[0]))] for _ in range(len(self._grid))]
        no_flashes  = False
        while not no_flashes:
            no_flashes = True
            for i in range(len(self._grid)):
                for j in range(len(self._grid)):
                    if self._grid[i][j] > 9 and not flashed[i][j]:
                        self._spread_flash(i, j)
                        no_flashes = False
                        flashed[i][j] = True
                        self._flashes += 1
        # set flashed to 0
        for i in range(len(flashed)):
            for j in range(len(flashed[i])):
                if flashed[i][j]:
                    self._grid[i][j] = 0


    def _spread_flash(self, i, j):
        # increment octopus around the flash
        surrounding = [(i-1, j), (i, j-1), (i-1, j-1), (i+1, j), (i, j+1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]
        for x, y in surrounding:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            else:
                # increment
                self._grid[x][y] += 1




def get_first_100_step_flashes(grid):
    octogrid = OctoGrid(grid)
    for _ in range(100):
        octogrid.step()
    return octogrid.flashes


def get_first_all_flash(grid):
    octogrid = OctoGrid(grid)
    steps = 0
    while True:
        if octogrid.all_flashed:
            break
        octogrid.step()
        steps += 1
    return steps

grid = [[int(x) for x in line] for line in input_text.strip().splitlines()]

print("Part 1")
print(f"First 100 step flashes: {get_first_100_step_flashes(grid)}")
print("Part 2")
print(f"First step where all octopus flash: {get_first_all_flash(grid)}")
