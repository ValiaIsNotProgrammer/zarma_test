import math
import sys
import time
from typing import Iterator
import multiprocessing

import numpy as np


def get_squares_v1(seq: Iterator[int]):
    numbers = [i for i in seq]
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares


def get_squares_v2(seq: Iterator[int]):
    squares = []
    for number in seq:
        squares.append(number ** 2)
    return squares


def get_squares_v3(seq: Iterator[int]):
    for number in seq:
        yield np.square(number, number)


def get_squares_v4(seq: Iterator[int]):
    return list(map(lambda x: x ** 2, seq))


def get_squares_v5(seq: Iterator[int]):
    return [number ** 2 for number in seq]


def get_squares_v6(seq: Iterator[int]):
    for number in seq:
        yield math.pow(number, 2)


def get_squares_v7(seq: Iterator[int]):
    for number in seq:
        yield number ** 2


def get_squares_v8(seq: Iterator[int]):
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        yield pool.map(lambda x: x ** 2, seq)



if __name__ == '__main__':
    name = sys.argv[1]
    func = globals()[name]
    seq = range(1, 1000001)
    start = time.monotonic_ns()
    result = func(seq)
    print(f'\tВремя работы {name}: {str(time.monotonic_ns() - start)} ms\n')
