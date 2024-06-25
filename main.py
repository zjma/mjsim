import random
from collections import Counter

# def win():
#     '''
#     My hand starts with one 9s but no 8s or 7s.
#     Do I eventually get a 789s/999s?
#     ~0.255
#     '''
#     tiles = ['9s'] * 3 + ['8s'] * 4 + ['7s'] * 4 + ['??'] * 112
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_9s = counts_by_tile.get('9s', 0)
#     num_8s = counts_by_tile.get('8s', 0)
#     num_7s = counts_by_tile.get('7s', 0)
#     return num_9s>=2 or num_8s>=1 and num_7s>=1

# def win():
#     '''
#     My hand starts with one 8s but no 9s/7s/6s.
#     Do I eventually get a 789s/678s/888s?
#     ~0.362
#     '''
#     tiles = ['9s']*4 + ['8s']*3 + ['7s']*4 + ['6s']*4 + ['??'] * 108
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_9s = counts_by_tile.get('9s', 0)
#     num_8s = counts_by_tile.get('8s', 0)
#     num_7s = counts_by_tile.get('7s', 0)
#     num_6s = counts_by_tile.get('6s', 0)
#     return num_8s>=2 or num_9s>=1 and num_7s>=1 or num_7s>=1 and num_6s>=1

# def win():
#     '''
#     My hand starts with one 7s but no 9s/8s/6s/5s.
#     Do I eventually get a 789s/678s/567s/777s?
#     ~0.472
#     '''
#     tiles = ['9s']*4 + ['8s']*4 + ['7s']*3 + ['6s']*4 + ['5s']*4 + ['??'] * 104
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_9s = counts_by_tile.get('9s', 0)
#     num_8s = counts_by_tile.get('8s', 0)
#     num_7s = counts_by_tile.get('7s', 0)
#     num_6s = counts_by_tile.get('6s', 0)
#     num_5s = counts_by_tile.get('5s', 0)
#     return num_7s>=2 or num_9s>=1 and num_8s>=1 or num_8s>=1 and num_6s>=1 or num_6s>=1 and num_5s>=1

# def win():
#     '''
#     My hand starts with one 1z.
#     Do I eventually get a 111z?
#     ~0.051
#     '''
#     tiles = ['1z']*3 + ['??'] * 120
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_1z = counts_by_tile.get('1z', 0)
#     return num_1z>=2

# def win():
#     '''
#     My hand starts with one 11z.
#     Do I eventually tsumo a 111z?
#     ~0.266
#     '''
#     tiles = ['1z']*2 + ['??'] * 121
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_1z = counts_by_tile.get('1z', 0)
#     return num_1z>=1

# def win():
#     '''
#     My hand starts with one 1z.
#     Do I eventually get a 11z?
#     ~0.370
#     '''
#     tiles = ['1z']*3 + ['??'] * 120
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_1z = counts_by_tile.get('1z', 0)
#     return num_1z>=1

# def win():
#     '''
#     My hand starts with one 89s but no 7s.
#     Do I eventually get a 789s?
#     ~0.462
#     '''
#     tiles = ['7s']*4 + ['??']*119
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_7s = counts_by_tile.get('7s', 0)
#     return num_7s>=1

def win():
    '''
    My hand starts with one 89s but no 7s.
    Do I get a 789s within 12 draws?
    ~0.339
    '''
    tiles = ['7s']*4 + ['??']*119
    assert len(tiles) == 123
    random.shuffle(tiles)
    available_to_draw = tiles[(13*3+14):]
    my_index = random.randint(0,3)
    my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index][:12]
    counts_by_tile = Counter(my_draws)
    num_7s = counts_by_tile.get('7s', 0)
    return num_7s>=1

def win():
    '''
    My hand starts with one 89s but no 7s.
    Do I get a 789s within 6 draws?
    ~0.181
    '''
    tiles = ['7s']*4 + ['??']*119
    assert len(tiles) == 123
    random.shuffle(tiles)
    available_to_draw = tiles[(13*3+14):]
    my_index = random.randint(0,3)
    my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index][:6]
    counts_by_tile = Counter(my_draws)
    num_7s = counts_by_tile.get('7s', 0)
    return num_7s>=1

# def win():
#     '''
#     My hand starts with one 78s but no 6/9s.
#     Do I eventually get a 789s/678s?
#     ~0.716
#     '''
#     tiles = ['6s']*4 + ['9s']*4 + ['??']*115
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_6s = counts_by_tile.get('6s', 0)
#     num_9s = counts_by_tile.get('9s', 0)
#     return num_6s>=1 or num_9s>=1

# def win():
#     '''
#     My hand starts with one 78s but no 6/9s.
#     Do I get a 789s/678s within 12 draws?
#     ~0.570
#     '''
#     tiles = ['6s']*4 + ['9s']*4 + ['??']*115
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index][:12]
#     counts_by_tile = Counter(my_draws)
#     num_6s = counts_by_tile.get('6s', 0)
#     num_9s = counts_by_tile.get('9s', 0)
#     return num_6s>=1 or num_9s>=1

def win():
    '''
    My hand starts with one 78s but no 6/9s.
    Do I get a 789s/678s within 6 draws?
    ~0.339
    '''
    tiles = ['6s']*4 + ['9s']*4 + ['??']*115
    assert len(tiles) == 123
    random.shuffle(tiles)
    available_to_draw = tiles[(13*3+14):]
    my_index = random.randint(0,3)
    my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index][:6]
    counts_by_tile = Counter(my_draws)
    num_6s = counts_by_tile.get('6s', 0)
    num_9s = counts_by_tile.get('9s', 0)
    return num_6s>=1 or num_9s>=1

# def win():
#     '''
#     My hand starts with one 34567s.
#     Do I eventually get 2 sequences out of it?
#     0.826
#     '''
#     tiles = ['2s']*4 + ['8s']*4 + ['5s']*3 + ['??']*112
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_2s = counts_by_tile.get('2s', 0)
#     num_5s = counts_by_tile.get('5s', 0)
#     num_8s = counts_by_tile.get('8s', 0)
#     return num_2s>=1 or num_5s>=1 or num_8s>=1

# def win():
#     '''
#     My hand starts with 789m 89s 89p.
#     Do I eventually tsumo sanshoku?
#     ~0.203
#     '''
#     tiles = ['7s']*4 + ['7p']*4 + ['??']*115
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_7s = counts_by_tile.get('7s', 0)
#     num_7p = counts_by_tile.get('7p', 0)
#     return num_7s>=1 and num_7p>=1

# def win():
#     '''
#     My hand starts with 19m19s19p123z
#     Do I eventually tsumo kokoshimosu?
#     0.035
#     '''
#     tiles = ['1s']*3+['9s']*3+['1m']*3+['9m']*3+['1p']*3+['9p']*3+['1z']*3+['2z']*3+['3z']*3+['4z']*4+['5z']*4+['6z']*4+['7z']*4+['??']*80
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_7z = counts_by_tile.get('7z', 0)
#     num_6z = counts_by_tile.get('6z', 0)
#     num_5z = counts_by_tile.get('5z', 0)
#     num_4z = counts_by_tile.get('4z', 0)
#     num_3z = counts_by_tile.get('3z', 0)
#     num_2z = counts_by_tile.get('2z', 0)
#     num_1z = counts_by_tile.get('1z', 0)
#     num_9p = counts_by_tile.get('9p', 0)
#     num_1p = counts_by_tile.get('1p', 0)
#     num_9s = counts_by_tile.get('9s', 0)
#     num_1s = counts_by_tile.get('1s', 0)
#     num_9m = counts_by_tile.get('9m', 0)
#     num_1m = counts_by_tile.get('1m', 0)
#     return num_7z>=1 and num_6z>=1 and num_5z>=1 and num_4z>=1 and (num_1m>=1 or num_9m>=1 or num_1s>=1 or num_9s>=1 or num_1p>=1 or num_9p>=1 or num_1z>=1 or num_2z>=1 or num_3z>=1 or num_4z>=2 or num_5z>=2 or num_6z>=2 or num_7z>=2)

# def win():
#     '''
#     My hand starts with 19m19s19p123z
#     Do I eventually tenpai kokoshimosu?
#     0.245
#     '''
#     tiles = ['1s']*3+['9s']*3+['1m']*3+['9m']*3+['1p']*3+['9p']*3+['1z']*3+['2z']*3+['3z']*3+['4z']*4+['5z']*4+['6z']*4+['7z']*4+['??']*80
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     terminals = ['1s','9s','1m','9m','1p','9p','1z','2z','3z','4z','5z','6z','7z']
#     my_terminals = [tile for tile in (my_draws + terminals[:9]) if tile in terminals]
#     counts_by_tile = Counter(my_terminals)
#     missing_terminals = [val for val in terminals if counts_by_tile.get(val,0) == 0]
#     two_plus_copy_terminals = [val for val in terminals if counts_by_tile.get(val,0) >= 2]
#     return len(missing_terminals)==0 or len(missing_terminals)==1 and len(two_plus_copy_terminals)>=1

# def win():
#     '''
#     My hand starts with 19m19s19p123z
#     Do I tenpai kokoshimosu within 12 draws?
#     '''
#     tiles = ['1s']*3+['9s']*3+['1m']*3+['9m']*3+['1p']*3+['9p']*3+['1z']*3+['2z']*3+['3z']*3+['4z']*4+['5z']*4+['6z']*4+['7z']*4+['??']*80
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index][:12]
#     terminals = ['1s','9s','1m','9m','1p','9p','1z','2z','3z','4z','5z','6z','7z']
#     my_terminals = [tile for tile in (my_draws + terminals[:9]) if tile in terminals]
#     counts_by_tile = Counter(my_terminals)
#     missing_terminals = [val for val in terminals if counts_by_tile.get(val,0) == 0]
#     two_plus_copy_terminals = [val for val in terminals if counts_by_tile.get(val,0) >= 2]
#     return len(missing_terminals)==0 or len(missing_terminals)==1 and len(two_plus_copy_terminals)>=1

# def win():
#     '''
#     My hand starts with 19m19s19p1234z
#     Do I eventually tsumo kokoshimosu?
#     0.096
#     '''
#     tiles = ['1s']*3+['9s']*3+['1m']*3+['9m']*3+['1p']*3+['9p']*3+['1z']*3+['2z']*3+['3z']*3+['4z']*3+['5z']*4+['6z']*4+['7z']*4+['??']*81
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_7z = counts_by_tile.get('7z', 0)
#     num_6z = counts_by_tile.get('6z', 0)
#     num_5z = counts_by_tile.get('5z', 0)
#     num_4z = counts_by_tile.get('4z', 0)
#     num_3z = counts_by_tile.get('3z', 0)
#     num_2z = counts_by_tile.get('2z', 0)
#     num_1z = counts_by_tile.get('1z', 0)
#     num_9p = counts_by_tile.get('9p', 0)
#     num_1p = counts_by_tile.get('1p', 0)
#     num_9s = counts_by_tile.get('9s', 0)
#     num_1s = counts_by_tile.get('1s', 0)
#     num_9m = counts_by_tile.get('9m', 0)
#     num_1m = counts_by_tile.get('1m', 0)
#     return num_7z>=1 and num_6z>=1 and num_5z>=1 and (num_1m>=1 or num_9m>=1 or num_1s>=1 or num_9s>=1 or num_1p>=1 or num_9p>=1 or num_1z>=1 or num_2z>=1 or num_3z>=1 or num_4z>=1 or num_5z>=2 or num_6z>=2 or num_7z>=2)

# def win():
#     '''
#     My hand starts with one 1z.
#     Do I eventually get a 11z with non-zero pon/tsumo possibility?
#     0.185
#     '''
#     tiles = ['1z']*3 + ['??'] * 120
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_1z_pair_formed = False
#     for draw_idx,tile in enumerate(available_to_draw):
#         if tile!='1z': continue
#         if my_1z_pair_formed: return True
#         if draw_idx%4 == my_index:
#             my_1z_pair_formed = True
#     return False
#

def win():
    '''
    My hand starts with one 1z. Dora indicator is also 1z.
    Do I eventually get a 11z with non-zero pon/tsumo possibility?
    0.081
    '''
    tiles = ['1z']*2 + ['??'] * 121
    assert len(tiles) == 123
    random.shuffle(tiles)
    available_to_draw = tiles[(13*3+14):]
    my_index = random.randint(0,3)
    my_1z_pair_formed = False
    for draw_idx,tile in enumerate(available_to_draw):
        if tile!='1z': continue
        if my_1z_pair_formed: return True
        if draw_idx%4 == my_index:
            my_1z_pair_formed = True
    return False

# def win():
#     '''
#     My hand starts with 3467s.
#     Do I eventually get 2 sequences out of it?
#     0.474
#     '''
#     tiles = ['2s']*4 + ['8s']*4 + ['5s']*4 + ['??']*111
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_2s = counts_by_tile.get('2s', 0)
#     num_5s = counts_by_tile.get('5s', 0)
#     num_8s = counts_by_tile.get('8s', 0)
#     if num_5s == 0:
#         return num_2s>=1 and num_8s>=1
#     elif num_5s == 1:
#         return num_2s >=1 or num_8s>=1
#     else:
#         return True

# def win():
#     '''
#     My hand starts with 1245s.
#     Do I eventually get 2 sequences out of it?
#     0.267
#     '''
#     tiles = ['3s']*4 + ['6s']*4 + ['??']*115
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_3s = counts_by_tile.get('3s', 0)
#     num_6s = counts_by_tile.get('6s', 0)
#     if num_3s == 0:
#         return False
#     elif num_3s == 1:
#         return num_6s >=1
#     else:
#         return True

# def win():
#     '''
#     My hand starts with 2378s.
#     Do I eventually get 2 sequences out of it?
#     0.506
#     '''
#     tiles = ['1s']*4 + ['4s']*4 + ['6s']*4 + ['9s']*4 + ['??']*107
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_1s = counts_by_tile.get('1s', 0)
#     num_4s = counts_by_tile.get('4s', 0)
#     num_6s = counts_by_tile.get('6s', 0)
#     num_9s = counts_by_tile.get('9s', 0)
#     return num_1s + num_4s >= 1 and num_6s + num_9s >= 1
#
# def win():
#     '''
#     My hand starts with 2233s.
#     Do I eventually get 2 sequences out of it?
#     0.317
#     '''
#     tiles = ['1s']*4 + ['4s']*4 + ['??']*115
#     assert len(tiles) == 123
#     random.shuffle(tiles)
#     available_to_draw = tiles[(13*3+14):]
#     my_index = random.randint(0,3)
#     my_draws = [t for (i,t) in enumerate(available_to_draw) if i%4==my_index]
#     counts_by_tile = Counter(my_draws)
#     num_1s = counts_by_tile.get('1s', 0)
#     num_4s = counts_by_tile.get('4s', 0)
#     return num_1s + num_4s >= 2

num_samples = 10000
num_wins = 0
for _ in range(num_samples):
    if win():
        num_wins += 1
print(num_wins / num_samples)
