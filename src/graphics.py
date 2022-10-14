import matplotlib.pyplot as plt
from pathlib import Path


def draw_synch_D():
    file_path_practice_D = Path(Path.cwd().parent, "outputData", "synch_practice_D.txt")
    file_path_theoretic_D = Path(Path.cwd().parent, "outputData", "synch_theoretic_D.txt")

    bar_lambda = []
    bar_practice_D = []
    bar_theoretic_D = []

    for line in open(file_path_practice_D, "r"):
        bar_name, bar_height = line.split()
        bar_lambda.append(float(bar_name))
        bar_practice_D.append(float(bar_height))
    for line in open(file_path_theoretic_D, "r"):
        _, buf_theoretic_D = line.split()
        bar_theoretic_D.append(float(buf_theoretic_D))

    # print(bar_lambda)
    # print(bar_practice_D)

    plt.figure("Synchronous system average delay")
    plt.title("Average delay for SMD M|D|1 synchronize")
    plt.xlabel("lambda")
    plt.ylabel("average delay")
    plt.plot(bar_lambda, bar_practice_D, label='practice average delay')
    plt.plot(bar_lambda,bar_theoretic_D, label='theoretic average delay')

    plt.legend()
    plt.grid(True)
    # plt.show()


def draw_synch_N():
    file_path_practice_N = Path(Path.cwd().parent, "outputData", "synch_practice_N.txt")
    file_path_theoretic_N = Path(Path.cwd().parent, "outputData", "synch_theoretic_N.txt")

    bar_lambda = []  # [1,32,4,12,34,6,8,34,47]
    bar_practice_N = []  # [0,20,23,25,21,22,10,14,15]
    bar_theoretic_N = []

    for line in open(file_path_practice_N, "r"):
        buf_lambda, buf_N = line.split()
        bar_lambda.append(float(buf_lambda))
        bar_practice_N.append(float(buf_N))

    for line in open(file_path_theoretic_N, "r"):
        _, buf_theoretic_N = line.split()
        bar_theoretic_N.append(float(buf_theoretic_N))

    # print(bar_lambda)
    # print(bar_practice_N)

    plt.figure("Synchronous system average count users")
    plt.title("Average count users for SMD M|D|1 synchronize")
    plt.xlabel("lambda")
    plt.ylabel("average count users")
    plt.plot(bar_lambda, bar_practice_N, label='practice count users')
    plt.plot(bar_lambda, bar_theoretic_N, label='theoretic count users')

    plt.legend()
    plt.grid(True)
    # plt.show()


def draw_asynch_D():
    file_path_practice_D = Path(Path.cwd().parent, "outputData", "asynch_practice_D.txt")
    file_path_theoretic_D = Path(Path.cwd().parent, "outputData", "asynch_theoretic_D.txt")

    bar_lambda = []
    bar_practice_D = []
    bar_theoretic_D = []

    for line in open(file_path_practice_D, "r"):
        bar_name, bar_height = line.split()
        bar_lambda.append(float(bar_name))
        bar_practice_D.append(float(bar_height))
    for line in open(file_path_theoretic_D, "r"):
        _, buf_theoretic_D = line.split()
        bar_theoretic_D.append(float(buf_theoretic_D))

    # print(bar_lambda)
    # print(bar_practice_D)

    plt.figure("Asynchronous system average delay")
    plt.title("Average delay for SMD M|D|1 asynchronize")
    plt.xlabel("lambda")
    plt.ylabel("average delay")
    plt.plot(bar_lambda, bar_practice_D, label='practice average delay')
    plt.plot(bar_lambda, bar_theoretic_D, label='theoretic average delay')

    plt.legend()
    plt.grid(True)
    # plt.show()


def draw_asynch_N():
    file_path_practice_N = Path(Path.cwd().parent, "outputData", "asynch_practice_N.txt")
    file_path_theoretic_N = Path(Path.cwd().parent, "outputData", "asynch_theoretic_N.txt")

    bar_lambda = []
    bar_practice_N = []
    bar_theoretic_N = []

    for line in open(file_path_practice_N, "r"):
        buf_lambda, buf_N = line.split()
        bar_lambda.append(float(buf_lambda))
        bar_practice_N.append(float(buf_N))

    for line in open(file_path_theoretic_N, "r"):
        _, buf_theoretic_N = line.split()
        bar_theoretic_N.append(float(buf_theoretic_N))

    # print(bar_lambda)
    # print(bar_practice_N)

    plt.figure("Asynchronous system average count users")
    plt.title("Average count users for SMD M|D|1 asynchronize")
    plt.xlabel("lambda")
    plt.ylabel("average count users")
    plt.plot(bar_lambda, bar_practice_N, label='practice count users')
    plt.plot(bar_lambda, bar_theoretic_N, label='theoretic count users')

    plt.legend()
    plt.grid(True)
    # plt.show()


def draw_lambda():
    file_path_lambda_one = Path(Path.cwd().parent, "outputData", "lambda_one.txt")
    file_path_lambda_two = Path(Path.cwd().parent, "outputData", "lambda_t.txt")

    bar_lambda = []
    bar_lambda_out_one = []
    bar_lambda_out_two = []

    for line in open(file_path_lambda_one, "r"):
        buf_lambda, buf_N = line.split()
        bar_lambda.append(float(buf_lambda))
        bar_lambda_out_one.append(float(buf_N))

    for line in open(file_path_lambda_two, "r"):
        _, buf_theoretic_N = line.split()
        bar_lambda_out_two.append(float(buf_theoretic_N))

    # print(bar_lambda)
    # print(bar_practice_N)

    plt.figure("lambda input vs. lambda output")
    plt.title("lambda input vs. lambda output")
    plt.xlabel("lambda_input")
    plt.ylabel("lambda_output")
    plt.plot(bar_lambda, bar_lambda_out_one, label='window = 1')
    plt.plot(bar_lambda, bar_lambda_out_two, label='window = 2')

    plt.legend()
    plt.grid(True)
    plt.show()


def draw_all_graphics():
    draw_asynch_D()
    draw_asynch_N()
    draw_synch_N()
    draw_synch_D()
    plt.show()


if __name__ == "__main__":
    draw_all_graphics()
    # draw_lambda()
    # draw_asynch_D()
    # draw_asynch_N()
    # draw_synch_N()
    # draw_synch_D()