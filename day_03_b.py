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
            if data[row][col] == '*':
                symbol_coord.append((row, col))
            last_val = 'symbol'


# Create list of valid touching coordinates
touch_coords = []
for (row, col) in symbol_coord:
    touch_coords.append([(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col),
              (row - 1, col - 1), (row + 1, col - 1), (row - 1, col + 1), (row + 1, col + 1)])

# Evaluate which product nums are valid
total_gear_ratio = 0
for coord in touch_coords:
    gear_ratio = 1
    total_products = 0
    for (row, col) in number_dict:
        include = False
        for i in range(len(number_dict[(row, col)])):
            if (row, col + i) in coord:
                include = True
        if include:
            total_products += 1
            gear_ratio *= int(number_dict[(row, col)])
    if total_products == 2:
        total_gear_ratio += gear_ratio

print(f'Part B: {total_gear_ratio}')
