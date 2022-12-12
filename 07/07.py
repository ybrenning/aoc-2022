def part_one() -> None:
    with open("example.txt") as f:
        lines = f.readlines()
    
    dirs: dict[str, list[int | str]] = {}
    current_dir = "/"
    
    for i in range(0, len(lines)):
        if lines[i].startswith("$ cd") and lines[i].split(" ")[2].replace("\n", "") != "..":
            current_dir = lines[i].split(" ")[2].replace("\n", "")
            dirs[current_dir] = []
        elif lines[i].startswith("$ ls"):
            j = i + 1
            
            current_line = lines[j]
            while j < len(lines) and not current_line.startswith("$"):
                if current_line[0].isdigit():
                    dirs[current_dir].append(int(current_line.split(" ")[0]))
                elif current_line.startswith("dir"):
                    dirs[current_dir].append(current_line.split(" ")[1].replace("\n", ""))
                j += 1
                if j >= len(lines):
                    break
                
                current_line = lines[j]
    
    dir_sizes = {}
    for key in dirs.keys():
        dir_sizes[key] = 0

    for key in dirs.keys():
        if dir_sizes[key] == 0:
            fun(dir_sizes, dirs, key)

    print(sum([ds for ds in dir_sizes.values() if ds <= 100000]))


def fun(dir_sizes, dirs, dirname):
    for item in dirs[dirname]:
        if isinstance(item, str):
            dir_sizes[dirname] += fun(dir_sizes, dirs, item)
        elif isinstance(item, int):
            dir_sizes[dirname] += item
    
    return dir_sizes[dirname]



def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
