import re
from word2number import w2n
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_01_data.txt'
data_set = ReadFile(FILE_PATH).data_set


# Complete Part A
data_nums = []
row_num = 0
for line in data_set:
    line_nums = []
    for char in line:
        try:
            int(char)
            line_nums.append(char)
        except:
            pass
    row_num += int(line_nums[0] + line_nums[-1])

print(f'Part A: {row_num}')


def find_numbers_in_string(input_string):
    # Use regular expression to find words that represent numbers
    num_string = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    words = num_string.findall(input_string)

    # Convert the word representations to numeric values
    numbers = []
    for word in words:
        numbers.append(w2n.word_to_num(word))

    # Separate individual digits
    numbers_digitized = []
    for number in numbers:
        [numbers_digitized.append(digit) for digit in str(number)]

    return numbers_digitized


row_num = 0
for line in data_set:
    line_nums = find_numbers_in_string(line)
    row_num += int(str(line_nums[0]) + str(line_nums[-1]))

print(f'Part B {row_num}')