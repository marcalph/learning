import random
import secrets
import uuid
from statistics import mean
from statistics import stdev
import string
import time
import timeit



alphabet = string.ascii_lowercase + string.digits

def random_choice() -> str:
    return ''.join(random.choices(alphabet, k=8))


def truncated_uuid4() -> str:
    return str(uuid.uuid4())[:18]


def secrets_random_choice() -> str:
    return ''.join(secrets.choice(alphabet) for _ in range(8))


def check_collisions(fun):
    out = set()
    count = 0
    for _ in range(10_000_000):
        new = fun()
        if new in out:
            count += 1
        else:
            out.add(new)
    print(fun())
    return count


def run_and_print_results(fun):
    round_digits = 5
    now = time.time()
    collisions = check_collisions(fun)
    total_time = round(time.time() - now, round_digits)

    trials = 1_000
    runs = 100
    func_time = timeit.repeat(fun, repeat=runs, number=trials)
    avg = round(mean(func_time), round_digits)
    std = round(stdev(func_time), round_digits)

    print(f'{fun.__name__}: collisions {collisions} - '
          f'time (s) {avg} ± {std} - '
          f'total (s) {total_time}')


if __name__ == '__main__':
    run_and_print_results(random_choice)
    run_and_print_results(truncated_uuid4)
    run_and_print_results(secrets_random_choice)