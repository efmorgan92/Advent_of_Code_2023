import re
from classes.read_file import ReadFile

FILE_PATH = 'data_inputs/day_02_data.txt'
data_set = ReadFile(FILE_PATH).data_set


# Clean and sort data
game_cnt = 0
game_pwrs = []
for game in data_set:
    add_game_num = True
    color_max = {'red': 12, 'green': 13, 'blue': 14}
    color_min = {'red': 0, 'green': 0, 'blue': 0}

    game_num = int(game.split(':')[0].split("Game ")[1])
    ball_pulls = game.split(':')[1].split(';')
    for ball_pull in ball_pulls:
        for turn in ball_pull.split(","):
            ball_cnt, ball_color = re.findall(r'(blue|red|green|\d+)', turn)

            if int(ball_cnt) > color_max[ball_color]:
                add_game_num = False

            if int(ball_cnt) > color_min[ball_color]:
                color_min[ball_color] = int(ball_cnt)

    if add_game_num:
        game_cnt += game_num

    game_pwrs.append(color_min['red'] * color_min['green'] * color_min['blue'])

print(f'Part A: {game_cnt}')
print(f'Part B: {sum(game_pwrs)}')


