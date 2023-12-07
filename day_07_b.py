import re
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_07_data.txt'
data_set = ReadFile(FILE_PATH).data_set

card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'J']
hands = []
for line in data_set:
    hand = line.split(' ')[0]
    bid = int(line.split(' ')[1])
    hands.append([hand, bid])


def count_cards(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts.keys():
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    if 'J' in card_counts.keys():
        max_cnt = max(card_counts.values())
        for key, value in card_counts.items():
            if value == max_cnt and key != 'J':
                card_counts[key] += card_counts['J']
                card_counts['J'] = 1
                break
        if 1 < card_counts['J'] < 5:
            for key, value in card_counts.items():
                if key != 'J':
                    card_counts[key] += card_counts['J']
                    card_counts['J'] = 1
                    break
    return card_counts


def find_hand_type(hand):
    card_counts = count_cards(hand)
    max_card_cnt = max(card_counts.values())
    card_product = 1
    for cnt in card_counts.values():
        card_product *= cnt
    if max_card_cnt == 5:             # Five of a kind
        hand_type = 0
    elif max_card_cnt == 4:           # Four of a kind
        hand_type = 1
    elif max_card_cnt == 3:
        if 2 in card_counts.values(): # Full house
            hand_type = 2
        else:                         # Three of a kind
            hand_type = 3
    elif card_product == 4:           # Two pair
        hand_type = 4
    elif card_product == 2:           # One pair
        hand_type = 5
    else:                             # High card
        hand_type = 6
    print(f'Hand: {hand}, Type: {hand_type}')
    return hand_type


def sort_hands(hand_type_hands, ind):
    hand_order = []
    card_val = {}
    for hand in hand_type_hands:
        card_ord = card_order.index(hand[0][ind])
        if card_ord in card_val.keys():
            card_val[card_ord].append(hand)
        else:
            card_val[card_ord] = [hand]
    for value in sorted(card_val.keys()):
        if len(card_val[value]) > 1:
            inner_sort = sort_hands(card_val[value], ind + 1)
            [hand_order.append(inner_hand) for inner_hand in inner_sort]
        else:
            hand_order.append(card_val[value][0])
    return hand_order


hand_types = {}
for i in range(len(hands)):
    hand_type = find_hand_type(hands[i][0])
    if hand_type in hand_types.keys():
        hand_types[hand_type].append(hands[i])
    else:
        hand_types[hand_type] = [hands[i]]

hand_rank = []
for hand_type in sorted(hand_types.keys()):
    if len(hand_types[hand_type]) > 1:
        inner_ranks = sort_hands(hand_types[hand_type], 0)
        [hand_rank.append(inner_rank) for inner_rank in inner_ranks]
    else:
        hand_rank.append(hand_types[hand_type][0])

rank = len(hand_rank)

bid_score = 0
for j in range(len(hand_rank)):
    print(hand_rank[j])
    bid_score += hand_rank[j][1]*rank
    rank -= 1

print(f'Part B: {bid_score}')