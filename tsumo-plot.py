import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def draw_pile_size_to_round(draw_pile_size):
    return (69-draw_pile_size)/4 + 1


def num_waiting_to_color(num_waiting):
    return


colors = {}
for num_waiting in range(1, 12):
    r = num_waiting/11
    colors[num_waiting] = (r, 0, 1-r)


df = pd.read_csv('tsumo.csv')
df = df.sort_values(by='draw_pile_size', ascending=False)

plt.rcParams['font.sans-serif'] = ['SimHei']  # For Chinese characters
plt.rcParams['axes.unicode_minus'] = False    # To display the minus sign correctly

plt.figure(figsize=(10, 6))
for num_waiting, group in df.groupby('num_waiting'):
    round = draw_pile_size_to_round(group['draw_pile_size'])
    plt.plot(round, group['win_rate'], marker='o', label=f'听{num_waiting}枚', color=colors[num_waiting], markersize=2)

plt.xlabel('巡目')
plt.ylabel('自摸率')
plt.title('听牌枚数-巡目-自摸率')
plt.legend()
plt.grid(True)
#plt.gca().invert_xaxis()
plt.xticks([0, 3, 6, 9, 12, 15, 18])

plt.savefig(PNG_PATH)
#xunmu-draw_pile_size: 68,67,66 -> 1, 65-62 -> 2
