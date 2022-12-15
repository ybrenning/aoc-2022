#!/usr/bin/env python3

INF = 1_000_000


class Node:
    def __init__(self, x: int, y: int, elevation: str) -> None:
        self.coords = (x, y)
        self.elevation = elevation
        self.next: list[Node | None] = []

    def __repr__(self) -> str:
        return "Node(" + str(self.coords) + ", " + self.elevation + ")"


def bfs(nodes: list[list[Node]], src: Node | None, dest: Node | None) -> int:
    if not src or not dest:
        raise ValueError("Source and dest nodes not found")

    queue = []

    visited = [[] for _ in range(0, len(nodes))]
    dist = [[] for _ in range(0, len(nodes))]

    for y in range(0, len(nodes)):
        for _ in range(0, len(nodes[y])):
            visited[y].append(False)
            dist[y].append(INF)

    visited[src.coords[1]][src.coords[0]] = True
    dist[src.coords[1]][src.coords[0]] = 0
    queue.append(src)

    while len(queue) != 0:
        curr = queue.pop(0)
        (
            x,
            y,
        ) = curr.coords
        for i in range(0, len(curr.next)):
            xn, yn = curr.next[i].coords

            if not visited[yn][xn]:
                visited[yn][xn] = True
                dist[yn][xn] = dist[y][x] + 1
                queue.append(curr.next[i])

                if curr.next[i].coords == dest.coords:
                    return dist[yn][xn]

    return -1


def part_one() -> None:
    with open("input.txt") as f:
        lines = [
            line.strip().replace("\n", "")
            for line in f.readlines()
            if line.strip().replace("\n", "")
        ]

    # Create nodes
    start = None
    end = None

    nodes = []
    for y in range(0, len(lines)):
        nodes.append([])
        for x in range(0, len(lines[y])):
            elevation = lines[y][x].strip()
            if elevation == "S":
                start = Node(x, y, "a")
                nodes[y].append(start)
            elif elevation == "E":
                end = Node(x, y, "z")
                nodes[y].append(end)
            else:
                nodes[y].append(Node(x, y, elevation))

    # Get node paths
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            possible_nexts = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            possible_nexts = [
                coord
                for coord in possible_nexts
                if 0 <= coord[0] < len(lines[y]) and 0 <= coord[1] < len(lines)
            ]

            for coord in possible_nexts:
                # Get the reference to the possible next node
                xn, yn = coord
                possible_next = nodes[yn][xn]

                # Check whether it is accessible
                if ord(possible_next.elevation) - 1 <= ord(nodes[y][x].elevation):
                    nodes[y][x].next.append(possible_next)

    print(bfs(nodes, start, end))


def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
