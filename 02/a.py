import os
import re

limit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def main():
    # with open(os.path.join(os.path.dirname(__file__), "example.txt"), "r") as file:
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        content = file.read()

    print(parse(content))


def parse(content):
    ids = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        print("------")
        print("line:", i+1)
        info = line.split(":")
        pulls = info[1].split(";")
        r = 0
        g = 0
        b = 0

        gameId = i + 1

        possible = True

        for pull in pulls:
            cols = pull.strip().split(",")
            for col in cols:
                col = col.strip()
                print(col)
                de = col.split(" ")

                if int(de[0]) > limit[de[1]]:
                    possible = False

        if possible:
            ids.append(gameId)

    return sum(ids)


main()
