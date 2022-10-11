import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def draw_synch_D():
    file_path_D = Path(Path.cwd().parent, "outputData", "synch_practice_D.txt")

    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    bar_names = []  # [1,32,4,12,34,6,8,34,47]
    bar_heights = []  # [0,20,23,25,21,22,10,14,15]

    for line in open(file_path_D, "r"):
        bar_name, bar_height = line.split()
        bar_names.append(float(bar_name))
        bar_heights.append(float(bar_height))

    print(bar_names)
    print(bar_heights)

    plt.title("Average delay for SMD M|D|1 synchronize")
    plt.xlabel("lambda")
    plt.ylabel("average delay")
    plt.plot(bar_names, bar_heights)

    plt.show()


def draw_synch_N():
    file_path_N = Path(Path.cwd().parent, "outputData", "synch_practice_N.txt")

    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    bar_lambda = []  # [1,32,4,12,34,6,8,34,47]
    bar_N = []  # [0,20,23,25,21,22,10,14,15]

    for line in open(file_path_N, "r"):
        buf_lambda, buf_N = line.split()
        bar_lambda.append(float(buf_lambda))
        bar_N.append(float(buf_N))

    print(bar_lambda)
    print(bar_N)

    plt.title("Average count users for SMD M|D|1 synchronize")
    plt.xlabel("lambda")
    plt.ylabel("average count users")
    plt.plot(bar_lambda, bar_N)

    plt.show()


if __name__ == "__main__":
    draw_synch_D()
