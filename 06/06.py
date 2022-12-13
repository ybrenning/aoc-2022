def part_one() -> None:
    with open("input.txt") as f:
        line = f.readline()

    for i in range(0, len(line) - 4):
        if len(set(line[i : i + 4])) == len(line[i : i + 4]):
            print(i + 4)
            break


def part_two() -> None:
    with open("input.txt") as f:
        line = f.readline()

    for i in range(0, len(line) - 14):
        if len(set(line[i : i + 14])) == len(line[i : i + 14]):
            print(i + 14)
            break


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
