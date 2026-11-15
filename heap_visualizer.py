#!/usr/bin/env python3
"""Show binary min-heap snapshots after each inserted value."""

import argparse


def insert(heap: list[int], value: int) -> None:
    heap.append(value)
    index = len(heap) - 1
    while index > 0:
        parent = (index - 1) // 2
        if heap[parent] <= heap[index]:
            break
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent


def tree_lines(heap: list[int]) -> list[str]:
    lines = []
    level = 0
    start = 0
    while start < len(heap):
        count = 2 ** level
        values = heap[start:start + count]
        lines.append("level " + str(level) + ": " + "  ".join(map(str, values)))
        start += count
        level += 1
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("values", nargs="+", type=int)
    args = parser.parse_args()
    heap = []
    for value in args.values:
        insert(heap, value)
        print(f"insert {value}: {heap}")
    print("\n".join(tree_lines(heap)))


if __name__ == "__main__":
    main()
