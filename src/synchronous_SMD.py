import math
import queue
import random
from pathlib import Path
from message import Message

MAX_TIME = 500000

file_practice_D = None
file_theoretic_D = None
file_practice_N = None
file_theoretic_N = None
queue_messages = queue.Queue()
count_users = 0


# lambda_out = 0


def init_files():
    global file_practice_D
    global file_practice_N
    global file_theoretic_D
    global file_theoretic_N
    file_path_practic_D = Path(Path.cwd().parent, "outputData", "synch_practice_D.txt")
    file_path_theoretic_D = Path(Path.cwd().parent, "outputData", "synch_theoretic_D.txt")
    file_path_practic_N = Path(Path.cwd().parent, "outputData", "synch_practice_N.txt")
    file_path_theoretic_N = Path(Path.cwd().parent, "outputData", "synch_theoretic_N.txt")

    file_practice_D = open(file_path_practic_D, 'w')
    file_theoretic_D = open(file_path_theoretic_D, 'w')
    file_practice_N = open(file_path_practic_N, 'w')
    file_theoretic_N = open(file_path_theoretic_N, 'w')


def get_queue_size(my_lambda):
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
    size_queue = get_queue_size(my_lambda)
    # print("size_queue", size_queue)
    values = []
    for i in range(size_queue):
        values.append(random.random())
    values.sort()
    for i in range(size_queue):
        bf = Message(values[i] + t)
        queue_messages.put(bf)


def simulate_messaging(my_lambda):
    queue_messages.queue.clear()
    t = 0
    # global lambda_out
    global count_users
    sent_messages = []
    while t < MAX_TIME:
        if not queue_messages.empty():
            buffer_message = queue_messages.get()
            buffer_message.exit_time = t + 1
            sent_messages.append(buffer_message)
            # lambda_out += 1

        create_queue_messages(my_lambda, t)
        count_users += queue_messages.qsize()
        t += 1

    # for i in range(len(sent_messages)):
    #     sent_messages[i].print()
    #     print(sent_messages[i].exit_time - sent_messages[i].start_time)
    #     print()

    count_users /= MAX_TIME
    # lambda_out /= MAX_TIME
    return sent_messages


def get_average_practical_delay(my_lambda):
    delay = 0
    sent_message = []
    global count_users
    count_users = 0
    sent_message = simulate_messaging(my_lambda)
    for i in range(len(sent_message)):
        delay += sent_message[i].get_delta()  # sent_message[i].exit_time - sent_message[i].start_time

    print("delay = ", delay)
    average_delay = delay / len(sent_message)
    print("average delay = ", average_delay)
    print("\n")
    # if average_delay < 0:
    #     print("<0")
    #     for i in range(len(sent_message)):
    #         if sent_message[i].exit_time - sent_message[i].start_time < 0:
    #             print()
    #             sent_message[i].print()
    #             print(sent_message[i].get_delta())  # sent_message[i].exit_time - sent_message[i].start_time)
    #             print()
    #         else:
    #             sent_message[i].print()
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
    while my_lambda < 1:  # for my_lambda in range(0.05, 2, 0.05):
        file_practice_D.write(f"{round(my_lambda, 3)} {round(get_average_practical_delay(my_lambda), 4)}\n")
        file_theoretic_D.write(f"{round(my_lambda, 3)} {round(get_average_theoretical_delay(my_lambda), 4)}\n")
        file_practice_N.write(f"{round(my_lambda, 3)} {round(get_average_count_users(my_lambda), 4)}\n")
        file_theoretic_N.write(f"{round(my_lambda, 3)} {round(get_average_theoretical_count_users(my_lambda), 4)}\n")
        my_lambda += 0.05
    file_practice_D.close()
    file_practice_N.close()
    file_theoretic_D.close()
    file_theoretic_N.close()


if __name__ == "__main__":
    make()
    # print(get_average_practical_delay(0.9))
    # print(get_average_theoretical_delay(0.9))
