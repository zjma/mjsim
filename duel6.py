import argparse
import matplotlib.pyplot as plt
import os
import pandas as pd
import random
import seaborn as sns
import utils


SIM_NAME, _ = os.path.splitext(os.path.basename(__file__))
DATA_SET_NAME = f'{SIM_NAME}.csv'
PNG_PATH = f'{SIM_NAME}.png'


def sample():
    def all_data():
        draw_pile_size = 46
        for my_wait_count in range(20):
            for my_hand_power in [1000, 2000, 4000, 8000, 12000, 16000]:
                data_points = [utils.simulate_duel(my_index=1, oppo_index=3, draw_pile_size=draw_pile_size, my_wait_count=my_wait_count, my_hand_power=my_hand_power, i_may_get_off=True, oppo_wait_count=6, oppo_hand_power=8000, oppo_may_get_off=True) for _ in range(10000)]
                avg_score_diff = sum(data_points) / 10000
                yield (my_wait_count, my_hand_power, draw_pile_size, avg_score_diff)
    dataset = list(all_data())
    df = pd.DataFrame(dataset, columns=['my_wait_count', 'my_hand_power', 'draw_pile_size', 'avg_score_diff'])
    df.to_csv(DATA_SET_NAME, index=False)


def plot():
    df = pd.read_csv(DATA_SET_NAME)
    heatmap_data = df.pivot_table(index='my_wait_count', columns='my_hand_power', values='avg_score_diff')

    plt.rcParams['font.sans-serif'] = ['SimHei']  # For Chinese characters
    plt.rcParams['axes.unicode_minus'] = False    # To display the minus sign correctly

    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', center=0, fmt='.1f')

    plt.xlabel('我方打点')
    plt.ylabel('我方听牌枚数')
    plt.title('两家对日期望得点(我方南家，敌方北家，巡目7，我方摸铳弃，敌方摸铳弃，敌军打点8000听6枚，两家做牌独立)')
    plt.gca().invert_yaxis()
    plt.legend()
    plt.savefig(PNG_PATH)


if __name__=='__main__':
    sample()
    plot()
