def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    priorities = 0
    for line in lines:
        fst, snd = line[: len(line) // 2], line[len(line) // 2 :]

        for char in fst:
            if char in snd:
                if char.isupper():
                    priorities += ord(char) - 38
                elif char.islower():
                    priorities += ord(char) - 96
                break

    print(priorities)


def part_two() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    priorities = 0
    for i in range(0, len(lines), 3):
        for char in lines[i]:
            if char in lines[i + 1] and char in lines[i + 2]:
                if char.isupper():
                    priorities += ord(char) - 38
                elif char.islower():
                    priorities += ord(char) - 96
                break

    print(priorities)


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
