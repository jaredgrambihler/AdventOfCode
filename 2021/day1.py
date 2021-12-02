with open("input/day1input.txt") as f:
    text = f.read()

input_numbers = [int(x) for x in text.strip().splitlines()]

def num_increasing(numbers):
    increasing = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            increasing += 1
    return increasing

def get_windows(numbers):
    windows = []
    for i in range(len(numbers) - 2):
        cur_window = numbers[i] + numbers[i + 1] + numbers[i + 2]
        windows.append(cur_window)
    return windows

print("Part 1")
print(f"Increasing: {num_increasing(input_numbers)}")
print("Part 2")
print(f"Increasing: {num_increasing(get_windows(input_numbers))}")