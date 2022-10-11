import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

if __name__ == "__main__":
    file_path_D = Path(Path.cwd().parent, "outputData", "synch_practice_D.txt")

    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    bar_names = []  # [1,32,4,12,34,6,8,34,47]
    bar_heights = []  # [0,20,23,25,21,22,10,14,15]

    # fig = plt.figure()

    for line in open(file_path_D, "r"):
        bar_name, bar_height = line.split()
        bar_names.append(float(bar_name))
        bar_heights.append(float(bar_height))

    print(bar_names)
    print(bar_heights)

    plt.plot(bar_names, bar_heights)

    plt.show()
