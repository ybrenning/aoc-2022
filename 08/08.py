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


def part_two() -> None:
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    
    max = current_score = upview = downview = lview = rview = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            left = lines[i][:j]
            right = lines[i][j+1:]
            
            above = [num[j] for num in lines[:i]]
            below = [num[j] for num in lines[i+1:]]
            
            # View trees from correct perspective
            left, above = left[::-1], above[::-1]
            
            for tree in above:
                upview += 1
                if int(tree) >= int(lines[i][j]):
                    break
            
            for tree in below:
                downview += 1
                if int(tree) >= int(lines[i][j]):
                    break
            
            for tree in left:
                lview += 1
                if int(tree) >= int(lines[i][j]):
                    break
            
            for tree in right:
                rview += 1
                if int(tree) >= int(lines[i][j]):
                    break
            
            current_score = upview * downview * lview * rview
            max = current_score if current_score > max else max
            
            # Reset view counts
            upview = downview = lview = rview = 0
        
    print(max)


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
