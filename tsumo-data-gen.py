import random
import pandas as pd


def calc(num_waiting: int, draw_pile_size: int):
    '''
    @param num_waiting:
    '''
    win = 0
    for _ in range(10000):
        my_index = random.randint(0, 3)
        all_hidden_tiles = [True] * num_waiting + [False] * (draw_pile_size + 14 + 13 * 3)
        random.shuffle(all_hidden_tiles)
        draw_pile = all_hidden_tiles[:draw_pile_size]
        my_draws = [tile for i,tile in enumerate(draw_pile) if i%4==my_index]
        if any(my_draws):
            win += 1
    return win/10000

def all_data():
    for num_waiting in range(1, 12):
        for draw_pile_size in range(1, 68):
            win_rate = calc(num_waiting, draw_pile_size)
            print(f'num_waiting={num_waiting}, draw_pile_size={draw_pile_size}, win_rate={win_rate}')
            yield (num_waiting, draw_pile_size, win_rate)

dataset = list(all_data())
df = pd.DataFrame(dataset, columns=['num_waiting', 'draw_pile_size', 'win_rate'])
df.to_csv('tsumo.csv', index=False)
