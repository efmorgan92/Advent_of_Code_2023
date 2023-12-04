import re

# Read in data
from classes.read_file import ReadFile

FILE_PATH = 'data_samples/day_04_sample.txt'
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

# Part A: Count how many winners in playing nums:
total_card_score = 0
for card in range(len(winning_cards)):
    card_win_cnt = 0
    for number in playing_cards[card]:
        if number in winning_cards[card]:
            if card_win_cnt == 0:
                card_win_cnt = 1
            else:
                card_win_cnt *= 2
    total_card_score += card_win_cnt

print(f'Part A: {total_card_score}')
