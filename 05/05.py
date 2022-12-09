from itertools import zip_longest


def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()
    
    index, craterows = 0, []
    while not lines[index + 1].isspace():
        craterows.append(lines[index])
        index += 1
    
    amount_of_stacks = len([[] for x in lines[index].split(" ") if x.isdigit()])
    
    crates = []
    for craterow in craterows:
        for i in range(0, len(craterow), 4):
            if craterow[i:i+4].isspace():
                crates.append(None)
            else:
                crates.append(craterow[i:i+4])

    crates2d = []
    for i in range(0, len(crates), amount_of_stacks):
        crates2d.append(crates[i:i+amount_of_stacks])
    
    # Transpose
    crates2d = [list(filter(None,i)) for i in zip_longest(*crates2d)]
    for i in range(0, len(crates2d)):
        crates2d[i] = [x.replace(" ", "").replace("\n", "") for x in crates2d[i]]
    
    instructions = lines[index + 2:]
    
    for i in range (0, len(instructions)):
        # Get current instruction
        nums = [int(char) for char in instructions[i].split() if char.isdigit()]
        
        # Execute instruction
        for _ in range(0, nums[0]):
            crates2d[nums[2] - 1].insert(0, crates2d[nums[1] - 1].pop(0))
    
    for stack in crates2d:
        print(stack[0].replace("[", "").replace("]", ""), end="")


def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
