import math
# import queue
from alive_progress import alive_bar
from queueFIFO import QueueFIFO
import synchronous_SMD
import random
from pathlib import Path
from message import Message

MAX_TIME = 500000

file_practice_D = None
file_theoretic_D = None
file_practice_N = None
file_theoretic_N = None
queue_messages = QueueFIFO()
count_users = 0


def init_files():
    global file_practice_D
    global file_practice_N
    global file_theoretic_D
    global file_theoretic_N
    file_path_practic_D = Path(Path.cwd().parent, "outputData", "asynch_practice_D.txt")
    file_path_theoretic_D = Path(Path.cwd().parent, "outputData", "asynch_theoretic_D.txt")
    file_path_practic_N = Path(Path.cwd().parent, "outputData", "asynch_practice_N.txt")
    file_path_theoretic_N = Path(Path.cwd().parent, "outputData", "asynch_theoretic_N.txt")

    file_practice_D = open(file_path_practic_D, 'w')
    file_theoretic_D = open(file_path_theoretic_D, 'w')
    file_practice_N = open(file_path_practic_N, 'w')
    file_theoretic_N = open(file_path_theoretic_N, 'w')


def get_new_users(my_lambda):
    L = math.exp(-my_lambda)
    # L = math.pow(10, -5)
    p = 1.0
    k = 0
    while True:
        k += 1
        p *= random.random()
        if p < L:
            break
    return k - 1


def create_queue_messages(my_lambda, t):
    global queue_messages
    size_queue = synchronous_SMD.get_queue_size(my_lambda)  # get_new_users(my_lambda)
    # print("size_queue", size_queue)
    values = []
    for i in range(size_queue):
        values.append(random.random())
    values.sort()
    for i in range(size_queue):
        bf = Message(values[i] + t)
        queue_messages.put(bf)


def simulate_messaging(my_lambda):
    queue_messages.clear()
    t = 0
    global count_users
    sent_messages = []
    while t < MAX_TIME:
        if not queue_messages.empty():
            out_message = queue_messages.get_without_deleting()
            if out_message.exit_time <= t:
                queue_messages.get()
                sent_messages.append(out_message)

        create_queue_messages(my_lambda, t)
        if not queue_messages.empty():
            count_users += queue_messages.len() - 1  # если очередь не пуста, то так как мы
            # в асинхронном режиме, первый уже точно обслуживается
        else:
            count_users += queue_messages.len()
        for i in range(queue_messages.len()):  # просто назначаем топорно время выхода
            cur_message = queue_messages.get_without_deleting(index=i)
            if cur_message.exit_time == 0:
                cur_message.exit_time = cur_message.start_time + 1
        for i in range(queue_messages.len()):
            if i == 0:
                continue
            if queue_messages.get_without_deleting(index=(i - 1)).exit_time + 1 > queue_messages.get_without_deleting(
                    index=i).exit_time:
                queue_messages.get_without_deleting(index=i).exit_time = queue_messages.get_without_deleting(
                    index=(i - 1)).exit_time + 1
        t += 1

    count_users /= MAX_TIME
    return sent_messages


def get_average_practical_delay(my_lambda):
    delay = 0
    sent_message = []
    global count_users
    count_users = 0
    sent_message = simulate_messaging(my_lambda)
    for i in range(len(sent_message)):
        delay += sent_message[i].get_delta()  # sent_message[i].exit_time - sent_message[i].start_time

    # print("delay = ", delay)
    # print("len(sent_message = ", len(sent_message))
    # average_delay = delay / len(sent_message)
    # print("average delay = ", average_delay)
    # print("\n")
    return delay / len(sent_message)


def get_average_theoretical_delay(my_lambda):
    d = (my_lambda * (2 - my_lambda)) / (2 * (1 - my_lambda))
    return d / my_lambda + 0.5


def get_average_count_users(my_lambda):
    global count_users
    return count_users


def get_average_theoretical_count_users(my_lambda):
    n = (my_lambda * (2 - my_lambda)) / (2 * (1 - my_lambda))
    return n


def make():
    init_files()
    my_lambda = 0.05
    count_step = int(1 / 0.05 - 1)
    with alive_bar(count_step, dual_line=True) as bar:
        bar.text = '\t-> The asynchronous system working, please wait...'
        while my_lambda < 1:  # for my_lambda in range(0.05, 2, 0.05):
            # print("lambda = ", my_lambda)
            file_practice_D.write(f"{round(my_lambda, 3)} {round(get_average_practical_delay(my_lambda), 4)}\n")
            file_theoretic_D.write(f"{round(my_lambda, 3)} {round(get_average_theoretical_delay(my_lambda), 4)}\n")
            file_practice_N.write(f"{round(my_lambda, 3)} {round(get_average_count_users(my_lambda), 4)}\n")
            file_theoretic_N.write(f"{round(my_lambda, 3)} {round(get_average_theoretical_count_users(my_lambda), 4)}\n")
            my_lambda += 0.05
            bar()
    file_practice_D.close()
    file_practice_N.close()
    file_theoretic_D.close()
    file_theoretic_N.close()


if __name__ == "__main__":
    make()
    # print(get_average_practical_delay(0.9))
    # print(get_average_theoretical_delay(0.9))
