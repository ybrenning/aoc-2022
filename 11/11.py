def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    index, monkeys = -1, []
    for line in lines:
        current_line = line.strip()
        if current_line.startswith("Monkey"):
            index += 1
            monkeys.append([])
        else:
            if current_line.startswith("Starting"):
                monkeys[index].append(
                    [
                        x.replace(",", "")
                        for x in line.split()
                        if x.replace(",", "").isdigit()
                    ]
                )
            elif current_line.startswith("Operation"):
                _, operation = line.strip().split("=")
                monkeys[index].append(operation.strip())
            elif current_line.startswith("Test"):
                div = line.split()[-1]
                monkeys[index].append(div)
            elif current_line.startswith("If"):
                monkeys[index].append(line.strip()[-1])

    inspections = [0 for _ in range(0, len(monkeys))]
    for _ in range(0, 20):
        for i, monkey in enumerate(monkeys):
            while len(monkey[0]) != 0:
                inspections[i] += 1
                current_worry = int(monkey[0].pop(0))

                operator = monkey[1].split()[1]
                operand = int(monkey[1].replace("old", str(current_worry)).split()[-1])

                match operator:
                    case "+":
                        current_worry += operand
                    case "*":
                        current_worry *= operand

                current_worry //= 3
                if current_worry % int(monkey[2]) == 0:
                    monkeys[int(monkey[3])][0].append(current_worry)
                else:
                    monkeys[int(monkey[4])][0].append(current_worry)

    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])


def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
