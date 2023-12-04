import re

# Read in data
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_04_data.txt'
data_set = ReadFile(FILE_PATH).data_set

# Split data into winning & playing numbers
winning_cards = []
playing_cards = []
card_ids = []
for line in data_set:
    card_ids.append(re.findall(r'\d+',line.split(':')[0])[0])
    cards = line.split(':')[1].split('|')
    winning_cards.append(re.findall(r'\d+', cards[0]))
    playing_cards.append(re.findall(r'\d+', cards[1]))

# Create a dictionary of card IDs and # of wins
card_dict = {}
for id in card_ids:
    index = int(id) - 1
    win_count = 0
    for number in playing_cards[index]:
        if number in winning_cards[index]:
            win_count += 1
    card_dict[int(id)] = [win_count, 1]

# Multiply cards based on wins
for card in card_dict:
    win_count = card_dict[card][0]
    card_to_add = card
    while win_count > 0:
        card_to_add += 1
        card_dict[card_to_add] = [card_dict[card_to_add][0], card_dict[card_to_add][1]+1*card_dict[card][1]]
        win_count -= 1

# Find the total number of cards
total_cards = 0
for card in card_dict:
    total_cards += card_dict[card][1]

print(f'Part B: {total_cards}')