from collections import defaultdict


def part_one() -> None:
    with open("input.txt") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip().split())
        
        signals = defaultdict(int)
        cycle, x = 0, 1
        cycle_count = 20
        for line in lines:
            if line[0] == "noop":
                cycle += 1
                if cycle == cycle_count:
                    signals[cycle_count] = cycle * x
                    cycle_count += 40
            elif line[0] == "addx":
                cycle += 1
                if cycle == cycle_count:
                    signals[cycle_count] = cycle * x
                    cycle_count += 40

                cycle += 1
                if cycle == cycle_count:
                    signals[cycle_count] = cycle * x
                    cycle_count += 40
                x += int(line[1])

    print(sum(signals.values()))
            

def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
