#!/usr/bin/python3
from sys import argv


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def isprime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def read_file(path: str) -> list[int]:
    with open(path, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: int(x), lines))


def pollards_rho(n: int) -> int:
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
    while not isprime(d):
        d = pollards_rho(d)
    return d, number // d


def main() -> None:

    if len(argv) != 2:
        print("Usage: factors <file>")
        return

    path_file = argv[1]
    numbers = read_file(path_file)
    for number in numbers:
        first, second = factorize_number(number)
        print("{:d}={:d}*{:d}".format(number, first, second))


if __name__ == '__main__':
    main()
