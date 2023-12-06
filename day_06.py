import re
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_06_data.txt'
data_set = ReadFile(FILE_PATH).data_set

# Part A
time = [int(item) for item in re.findall(r'\d+', data_set[0])]
distance = [int(item) for item in re.findall(r'\d+', data_set[1])]

race_results = 1
for i in range(len(time)):
    race_wins = 0
    for j in range(time[i]):
        if j*(time[i] - j) > distance[i]:
            race_wins += 1
    race_results *= race_wins

print(f'Part A: {race_results}')

# Part B
time = int(''.join(re.findall(r'\d+', data_set[0])))
distance = int(''.join(re.findall(r'\d+', data_set[1])))

race_wins = 0
for j in range(time):
    if j*(time - j) > distance:
        race_wins += 1

print(f'Part B: {race_wins}')
