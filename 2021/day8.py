from collections import Counter

with open("input/day8input.txt") as f:
    input_text = f.read()

lines = []

for line in input_text.strip().splitlines():
    signal_patterns, output = line.split("|")
    lines.append((signal_patterns.strip(), output.strip()))


def get_unique_digit_counts(lines):
    unqiue_lengths = set([2, 4, 3, 7])
    unique_digits = 0
    for _, output in lines:
        for output_number in output.split(" "):
            if len(output_number.strip()) in unqiue_lengths:
                unique_digits += 1
    return unique_digits


class Pattern:

    def __init__(self, chars):
        """chars is an array with the index corresponding to the numbers as follows

            0
          1   2
            3
          4   5
            6
        """
        self.chars = chars
    
    def get_num(self, num_str):
        indexes = set(self.chars.index(c) for c in num_str)
        if indexes == set([0, 1, 2, 4, 5, 6]):
            return 0
        if indexes == set([2, 5]):
            return 1
        elif indexes == set([0, 2,3,4,6]):
            return 2
        elif indexes == set([0, 2, 3, 5, 6]):
            return 3
        elif indexes == set([1, 2, 3, 5]):
            return 4
        elif indexes == set([0, 1, 3, 5, 6]):
            return 5
        elif indexes == set([0, 1, 3, 4, 5, 6]):
            return 6
        elif indexes == set([0, 2, 5]):
            return 7
        elif indexes == set([0,1,2,3,4,5,6]):
            return 8
        elif indexes == set([0,1,2,3,5,6]):
            return 9


def get_count_to_letters(signal_pattern):
    """Get count to letters.
    We know that across all 10 digits, each spot will have the number of occurences as shown below

            8
          6   8
            7
          4   9
            7
    """
    letter_to_count = Counter()
    for pattern in signal_pattern.split():
        for c in pattern.strip():
            letter_to_count[c] += 1
    count_to_letters = dict()
    for letter, count in letter_to_count.items():
        letters = count_to_letters.get(count, set())
        letters.add(letter)
        count_to_letters[count] = letters
    return count_to_letters


def find_pattern(signal_pattern) -> Pattern:
    def update_set(char_index_to_possible, char_set, indexes):
        # all indexes can only contain these chars
        for index in indexes:
            char_index_to_possible[index] = char_index_to_possible[index].intersection(char_set)
        # all other indexes can't contain these chars
        for i in range(7):
            if i not in indexes:
                char_index_to_possible[i] = char_index_to_possible[i] - char_set
    
    char_index_to_possible = {i: set(['a','b','c','d','e','f','g']) for i in range(7)}

    count_to_letters = get_count_to_letters(signal_pattern)
    char_index_to_count = {0: 8, 1: 6, 2: 8, 3: 7, 4: 4, 5: 9, 6: 7}
    for index, count in char_index_to_count.items():
        posisble_letters = count_to_letters[count]
        char_index_to_possible[index] = char_index_to_possible[index].intersection(posisble_letters)

    for pattern in signal_pattern.split():
        pattern = pattern.strip()
        cur_chars = set([c for c in pattern])
        if len(pattern) == 2:
            update_set(char_index_to_possible, cur_chars, [2,5])
        elif len(pattern) == 3:
            update_set(char_index_to_possible, cur_chars, [0,2,5])
        elif len(pattern) == 4:
            update_set(char_index_to_possible, cur_chars, [1,2,3,5])
        elif len(pattern) == 5:
            # 5 gives no information
            pass
        elif len(pattern) == 6:
            # 6 gives no information
            pass
        elif len(pattern) == 7:
            # 8 gives us no info
            pass
    chars = [None for _ in range(7)]
    for index, char_set in char_index_to_possible.items():
        assert len(char_set) == 1
        chars[index] = list(char_set)[0]
    return Pattern(chars)


def get_line_value(signal_patterns, output):
    pattern = find_pattern(signal_patterns)
    nums = []
    for output_num in output.split():
        nums.append(pattern.get_num(output_num))
    return int("".join(str(num) for num in nums))


def sum_output_values(lines):
    total_sum = 0
    for signal_patterns, output in lines:
        total_sum += get_line_value(signal_patterns, output)
    return total_sum

print("Part 1")
print(f"Unique digit counts: {get_unique_digit_counts(lines)}")
print("Part 2")
print(f"Total sum: {sum_output_values(lines)}")
