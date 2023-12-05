import re

# Read in data
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_05_data.txt'
data_set = ReadFile(FILE_PATH).data_set

map_titles = ['seed-to-soil map:',
              'soil-to-fertilizer map:',
              'fertilizer-to-water map:',
              'water-to-light map:',
              'light-to-temperature map:',
              'temperature-to-humidity map:',
              'humidity-to-location map:']

seeds = [int(seed) for seed in re.findall(r'\d+', data_set[0])]
seed_ranges = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
max_seed = max([seed[0]+seed[1] for seed in seed_ranges])


maps = []
map_indexes = [data_set.index(map_title) for map_title in map_titles]
for i in range(len(map_indexes)):
    if i != len(map_indexes)-1:
        maps.append(data_set[map_indexes[i]+1: map_indexes[i+1]-1])
    else:
        maps.append(data_set[map_indexes[i]+1:])
total_length = 0
for line in maps:
    total_length += len(line)


map_dicts = []
for mapping in maps:
    map_dict = []
    for line in mapping:
        map_dict.append([int(line_num) for line_num in re.findall(r'\d+', line)])
    map_dict = sorted(map_dict, key=lambda x: x[1])

    map_final = []
    start = 0
    i = 0
    while start < (map_dict[-1][1] + map_dict[-1][2]):
        if map_dict[i][1] > start:
            map_final.append([start, start, map_dict[i][1] - start])
            start = map_dict[i][1]
        else:
            map_final.append(map_dict[i])
            start = map_dict[i][2] + map_dict[i][1]
            i += 1
    if max_seed > start:
        map_final.append([start, start, max_seed + 1 - start])
    map_final = sorted(map_final, key=lambda x: x[1])
    map_dicts.append(map_final)


def start_in_range(seed, map_rule):
    if seed[0] >= map_rule[1] and seed[0] < map_rule[1] + map_rule[2]:
        return True
    else: return False


def end_in_range(seed, map_rule):
    if (seed[0] + seed[1]) <= (map_rule[1] + map_rule[2]):
        return True
    else: return False


def output_mapping(seed_in_range, map_rule):
    return [seed_in_range[0] - map_rule[1] + map_rule[0], seed_in_range[1]]


def split_seeds(seed_end_out_of_range, map_rule):
    allowed_range = map_rule[1]+map_rule[2]-seed_end_out_of_range[0]
    return [[seed_end_out_of_range[0], allowed_range],
            [map_rule[1] + map_rule[2], seed_end_out_of_range[1] - allowed_range]]


def eval_seed(seed_range, map_rule):
    if start_in_range(seed_range, map_rule):
        if end_in_range(seed_range, map_rule):
            return 'Complete'
        else:
            return 'Partial'
    return 'No Match'


def eval_current_layer(seed_ranges, map_dict):
    new_seed_ranges = []
    for seed_range in seed_ranges:
        for map_rule in map_dict:
            status = eval_seed(seed_range, map_rule)
            if status == 'Complete':
                new_seed_ranges.append(output_mapping(seed_range,map_rule))
            elif status == 'Partial':
                first_seed, second_seed = split_seeds(seed_range, map_rule)
                new_seed_ranges.append(output_mapping(first_seed,map_rule))
                seed_range = second_seed

    return new_seed_ranges


new_seed_ranges = seed_ranges
for map_dict in map_dicts:
    new_seed_ranges = eval_current_layer(new_seed_ranges, map_dict)

min_location = min([seed[0] for seed in new_seed_ranges])
print(f'Part B: {min_location}')