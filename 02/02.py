from enum import Enum


class Symbols(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcomes(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


ALIAS_SYMBOLS = {
    "A": Symbols.ROCK,
    "B": Symbols.PAPER,
    "C": Symbols.SCISSORS,
    "X": Symbols.ROCK,
    "Y": Symbols.PAPER,
    "Z": Symbols.SCISSORS
}

ALIAS_OUTCOMES = {
    "X": Outcomes.LOSE,
    "Y": Outcomes.DRAW,
    "Z": Outcomes.WIN
}

COMBINATIONS = {
    (Symbols.ROCK, Symbols.ROCK): Outcomes.DRAW,
    (Symbols.ROCK, Symbols.PAPER): Outcomes.LOSE,
    (Symbols.ROCK, Symbols.SCISSORS): Outcomes.WIN,
    
    (Symbols.PAPER, Symbols.ROCK): Outcomes.WIN,
    (Symbols.PAPER, Symbols.PAPER): Outcomes.DRAW,
    (Symbols.PAPER, Symbols.SCISSORS): Outcomes.LOSE,
    
    (Symbols.SCISSORS, Symbols.ROCK): Outcomes.LOSE,
    (Symbols.SCISSORS, Symbols.PAPER): Outcomes.WIN,
    (Symbols.SCISSORS, Symbols.SCISSORS): Outcomes.DRAW
}


def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()
    
    score = 0
    for line in lines:  
        match line[2]:
            case "X":
                score += 1
                match line[0]:
                    case "A":
                        score += 3
                    case "C":
                        score += 6
            case "Y":
                score += 2
                match line[0]:
                    case "A":
                        score += 6
                    case "B":
                        score += 3
            case "Z":
                score += 3
                match line[0]:
                    case "B":
                        score += 6
                    case "C":
                        score += 3
        
    print(score)


def part_two() -> None:
    with open("input.txt") as f:
        lines = f.readlines()
    
    score = 0
    for line in lines:
        status = ALIAS_OUTCOMES[line[2]]
        
        score += status.value
        if status == Outcomes.DRAW:
            score += ALIAS_SYMBOLS[line[0]].value
        elif status == Outcomes.WIN:
            for key, value in COMBINATIONS.items():
                if key[1] == ALIAS_SYMBOLS[line[0]] and value == status:
                    score += key[0].value
        elif status == Outcomes.LOSE:
            for key, value in COMBINATIONS.items():
                if key[1] == ALIAS_SYMBOLS[line[0]] and value == status:
                    score += key[0].value
    
    print(score) 


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
