import re

# Read in data
from classes.read_file import ReadFile

FILE_PATH = 'data_samples/day_05_samples.txt'
data_set = ReadFile(FILE_PATH).data_set

map_titles = ['seed-to-soil map:',
              'soil-to-fertilizer map:',
              'fertilizer-to-water map:',
              'water-to-light map:',
              'light-to-temperature map:',
              'temperature-to-humidity map:',
              'humidity-to-location map:']

seeds = [int(seed) for seed in re.findall(r'\d+', data_set[0])]

maps = []
map_indexes = [data_set.index(map_title) for map_title in map_titles]
for i in range(len(map_indexes)):
    if i != len(map_indexes)-1:
        maps.append(data_set[map_indexes[i]+1: map_indexes[i+1]-1])
    else:
        maps.append(data_set[map_indexes[i]+1:])

map_dicts = []
for mapping in maps:
    map_dict = []
    for line in mapping:
        map_dict.append([int(line_num) for line_num in re.findall(r'\d+', line)])
    map_dict = sorted(map_dict, key=lambda x: x[1])
    map_dicts.append(map_dict)

seed_location = {}
for seed in seeds:
    seed_proxy = seed
    for map_dict in map_dicts:
        seed_round = seed_proxy
        for rule in map_dict:
            if seed_round < rule[1]:
                break
            if rule[1] <= seed_round < (rule[1] + rule[2]):
                seed_proxy = seed_proxy - rule[1] + rule[0]
    seed_location[seed] = seed_proxy

print(seed_location)
print(f'Part A: {min(seed_location.values())}')








