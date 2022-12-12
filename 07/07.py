from collections import defaultdict

def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    sizes: dict[str, int] = defaultdict(int)
    filepath: list[str] = []

    for line in lines:
        if(line.startswith("$ cd")):
            dir = line.split()[-1]
            if(dir == ".."):
                filepath.pop()
            else:
                filepath.append(dir)
        elif(line.startswith("$ ls")):
            continue
        else:
            if(line.split()[0].isdigit()):
                size = int(line.split()[0])
                for i in range(0, len(filepath)):
                    sizes["/".join(filepath[:i+1])] += size
                    
    print(sum([size for size in sizes.values() if size <= 100_000]))


def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
