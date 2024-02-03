#!/usr/bin/python3
from sys import argv


def read_file(path: str) -> list[int]:
    with open(path, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: int(x), lines))


def factorize_number(number: int) -> tuple(int, int):
    pass


def main() -> None:
    path_file = argv[1]
    print(read_file(path=path_file))
    print("Hello python")


if __name__ == '__main__':
    main()
