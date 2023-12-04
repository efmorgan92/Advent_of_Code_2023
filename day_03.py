# Read in data
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_03_data.txt'
data_set = ReadFile(FILE_PATH).data_set

# Format data as array
data = []
number_dict = {}
symbol_coord = []

for line in data_set:
    data.append([char for char in line])

# Separate numbers and symbols
last_val = 'symbol'
current_product_num = ''
start_coords = (0, 0)

for row in range(len(data)):
    last_val = 'symbol'
    for col in range(len(data[row])):
        try:
            int(data[row][col])
            if last_val == 'number':
                current_product_num += data[row][col]
            else:
                start_coords = (row, col)
                current_product_num = data[row][col]
                last_val = 'number'
            number_dict[start_coords] = current_product_num
        except:
            if data[row][col] != '.':
                symbol_coord.append((row, col))
            last_val = 'symbol'


# Create list of valid touching coordinates
touch_coords = []
for (row, col) in symbol_coord:
    coords = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col),
              (row - 1, col - 1), (row + 1, col - 1), (row - 1, col + 1), (row + 1, col + 1)]
    [touch_coords.append(coord) for coord in coords]

# Evaluate which product nums are valid
product_num_sum = 0
for (row, col) in number_dict:
    include = False
    for i in range(len(number_dict[(row, col)])):
        if (row, col + i) in touch_coords:
            include = True
    if include:
        product_num_sum += int(number_dict[(row, col)])

print(f'Part A: {product_num_sum}')
