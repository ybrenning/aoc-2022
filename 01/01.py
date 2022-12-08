def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    curr = max = 0
    for line in lines:
        if line == "\n":
            max = curr if curr > max else max
            curr = 0
        else:
            curr += int(line)
    
    print(max)


def part_two() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    curr, top = 0, []
    for line in lines:
        if line == "\n":
            top.append(curr)
            curr = 0
        else:
            curr += int(line)
    
    top.sort(reverse=True)
    print(sum(top[:3]))


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
