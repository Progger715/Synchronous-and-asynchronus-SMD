import math
# import queue
import queueFIFO
import random
from pathlib import Path
from message import Message

MAX_MESSAGE = 10000

file_practice_D = None
file_theoretical_D = None
file_practice_N = None
queue_messages = queueFIFO.QueueFIFO()
total_time = 0
count_users = 0
lambda_out = 0


def init_files():
    global file_practice_D
    global file_practice_N
    global file_theoretical_D
    file_path_practic_D = Path(Path.cwd().parent, "outputData", "asynch_practice_D.txt")
    file_path_N = Path(Path.cwd().parent, "outputData", "asynch_practice_N.txt")
    file_path_theoretic_D = Path(Path.cwd().parent, "outputData", "asynch_theoretical_D.txt")
    file_practice_D = open(file_path_practic_D, 'w')
    file_theoretical_D = open(file_path_theoretic_D, "w")
    file_practice_N = open(file_path_N, 'w')


def create_queue_messages(my_lambda):
    global queue_messages
    queue_messages.put(Message(0.0))
    t = 0
    i = 0
    while i != MAX_MESSAGE:
        cur = (-1 * math.log(random.random()) / my_lambda)
        # if cur < 0:
        # print(f"cur = {cur}\tt = {t}")
        # print(f"{t + cur}\n")
        queue_messages.put(Message(t + cur))
        t += cur
        i += 1


def simulate_messaging(my_lambda):
    queue_messages.clear()
    create_queue_messages(my_lambda)
    global lambda_out
    sent_messages = []
    # queue_messages.print_all_message()
    queue_messages_exit = queueFIFO.QueueFIFO()
    queue_messages_exit.put(Message(0))
    global total_time
    total_time = 0
    sending_time = 0
    while not queue_messages.empty():
        # print(queue_messages.len())
        cur_message = queue_messages.get_without_deleting()
        if sending_time + 1 < cur_message.start_time:
            total_time = sending_time + 1
            sending_time += 1
            if not queue_messages_exit.empty():
                cur_message_exit = queue_messages_exit.get()
                cur_message_exit.exit_time = total_time
                sent_messages.append(cur_message_exit)
                # cur_message.print()
                lambda_out += 1
        elif sending_time + 1 > cur_message.start_time:
            cur_message = queue_messages.get()
            total_time = cur_message.start_time
            if not queue_messages_exit.empty():
                sending_time = total_time
            queue_messages_exit.put(cur_message)
        elif sending_time + 1 == cur_message.start_time:
            cur_message = queue_messages.get()
            total_time = cur_message.start_time
            if not queue_messages_exit.empty():
                cur_message_exit = queue_messages_exit.get()
                cur_message.exit_time = total_time
                sent_messages.append(cur_message)
                cur_message.print()
                lambda_out += 1
            if queue_messages_exit.empty():
                sending_time = total_time
            queue_messages_exit.put(cur_message)
    return sent_messages


def get_average_practice_delay(my_lambda):
    delay = 0
    sent_message = simulate_messaging(my_lambda)
    for i in range(len(sent_message)):
        delay += sent_message[i].get_delta()
        if i == len(sent_message) - 1:
            max_time = sent_message[i].exit_time
    return delay / len(sent_message)


def get_average_theoretical_delay(my_lambda):
    n = (my_lambda * (2 - my_lambda)) / (2 * (1 - my_lambda))
    return n


def get_average_count_users(my_lambda):
    return count_users


def make():
    init_files()
    my_lambda = 0.05
    while my_lambda < 1:
        file_practice_D.write(f"{round(my_lambda, 3)} {round(get_average_practice_delay(my_lambda), 4)}\n")
        file_practice_N.write(f"{my_lambda} {round(get_average_count_users(my_lambda), 4)}\n")
        file_theoretical_D.write(f"{round(my_lambda, 3)} {round(get_average_theoretical_delay(my_lambda), 4)}\n")
        my_lambda += 0.05
    file_practice_D.close()
    file_practice_N.close()


if __name__ == "__main__":
    make()
