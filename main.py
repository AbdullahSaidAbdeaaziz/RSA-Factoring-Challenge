#!/usr/bin/python3
from sys import argv


def read_file(path: str) -> list[int]:
    with open(path, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: int(x), lines))


def factorize_number(number: int) -> tuple[int, int]:
    for i in range(2, int(number**0.5) + 1):
        if number % i:
            continue
        else:
            return (i, number // i)
    return (number, 1)


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
