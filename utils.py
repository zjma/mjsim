import random


def simulate_duel(
        my_index: int, oppo_index: int, draw_pile_size: int,
        my_wait_count: int, my_hand_power: int, i_may_get_off: bool,
        oppo_wait_count: int, oppo_hand_power: int, oppo_may_get_off: bool):
    assert my_index != oppo_index
    tiles = [0]*(draw_pile_size+14+13*4) # last 13: my hand, last 26-13, oppo hand
    all_indices = set(range(draw_pile_size+14+13*4))
    oppo_hand_indices = set(range(draw_pile_size+14+13*2, draw_pile_size+14+13*3))
    my_hand_indices = set(range(draw_pile_size+14+13*3, draw_pile_size+14+13*4))

    # where are my winning tiles?
    for idx in random.sample(sorted(all_indices-my_hand_indices), my_wait_count):
        tiles[idx] |= 1

    # where are oppo's winning tiles?
    for idx in random.sample(sorted(all_indices-oppo_hand_indices), oppo_wait_count):
        tiles[idx] |= 2

    draw_pile = tiles[:draw_pile_size]
    i_gave_up = False
    oppo_gave_up = False

    for idx,tile in enumerate(draw_pile):
        player_in_action = (70 - draw_pile_size + idx) % 4
        if player_in_action == my_index:
            if (tile & 1) > 0 and not i_gave_up:
                return my_hand_power
            if (tile & 2) > 0:
                if i_may_get_off:
                    i_gave_up = True
                if not i_gave_up:
                    return -oppo_hand_power
        if player_in_action == oppo_index:
            if (tile & 2) > 0 and not oppo_gave_up:
                if my_index == 0:
                    return -oppo_hand_power/2
                else:
                    return -oppo_hand_power/4
            if (tile & 1) > 0:
                if oppo_may_get_off:
                    oppo_gave_up = True
                if not oppo_gave_up:
                    return my_hand_power

    if i_gave_up and oppo_gave_up:
        return 0
    elif i_gave_up and not oppo_gave_up:
        return -1000
    elif not i_gave_up and oppo_gave_up:
        return 3000
    else:
        return 1500
