from pathlib import Path

file_practice_D = None
file_practice_N = None


def init_files():
    global file_practice_D
    global file_practice_N
    file_path_D = Path(Path.cwd().parent, "outputData", "asynch_practice_D.txt")
    file_path_N = Path(Path.cwd().parent, "outputData", "asynch_practice_N.txt")
    file_practice_D = open(file_path_D, 'w')
    file_practice_N = open(file_path_N, 'w')


def get_average_delay(my_lambda):
    pass


def get_average_count_users(my_lambda):
    pass


def make():
    init_files()
    for my_lambda in range(0.05, 2, 0.05):
        file_practice_D.write(f"{my_lambda} {get_average_delay(my_lambda)}\n")
        file_practice_N.write(f"{my_lambda} {get_average_count_users(my_lambda)}\n")
