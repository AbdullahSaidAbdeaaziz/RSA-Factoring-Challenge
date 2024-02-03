#!/usr/bin/python3
from sys import argv
from math import gcd


def read_file(path: str) -> list[int]:
    with open(path, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: int(x), lines))


def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    return d


def factorize_number(number: int) -> tuple[int, int]:
    d = pollards_rho(number)
    if d == number:
        return number, 1
    else:
        return d, number // d


def main() -> None:

    if len(argv) != 2:
        print("Usage: factors <file>")
        return

    path_file = argv[1]
    numbers = read_file(path_file)
    for number in numbers:
        first, second = factorize_number(number)
        print(f"{number}={second}*{first}")


if __name__ == '__main__':
    main()
