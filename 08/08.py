def part_one() -> None:
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    
    count = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            left = lines[i][:j]
            right = lines[i][j+1:]
            
            above = [num[j] for num in lines[:i]]
            below = [num[j] for num in lines[i+1:]]
            
            if any(int(num) >= int(lines[i][j]) for num in left) and \
                any(int(num) >= int(lines[i][j]) for num in right) and \
                any(int(num) >= int(lines[i][j]) for num in above) and \
                any(int(num) >= int(lines[i][j]) for num in below):
                    continue
            else:
                count += 1
    
    print(count)


def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
