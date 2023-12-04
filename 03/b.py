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
    gamepower = []

    lines = content.split('\n')
    for i, line in enumerate(lines):

        print("------")
        print("line:", i+1)
        info = line.split(":")
        pulls = info[1].split(";")
        max = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for pull in pulls:
            cols = pull.strip().split(",")
            for col in cols:
                col = col.strip()
                de = col.split(" ")

                if int(de[0]) > max[de[1]]:
                    max[de[1]] = int(de[0])

        a = 1
        print(max)
        for key in max:
            a *= max[key]

        print(a)

        gamepower.append(a)

    return sum(gamepower)


main()
