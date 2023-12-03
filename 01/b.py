import os
import re


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        content = file.read()

    print(parse(content))


checker = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}


def parse(content):
    lines = content.splitlines()
    a = 0
    for i, line in enumerate(lines):

        strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        finds = re.findall(r'|'.join(strings), line)

        finds.sort(key=lambda x: line.index(x))

        first = finds[0]
        last = finds[-1]

        print("line:", i+1)
        print(first, last)

        try:
            first = int(first)
        except:
            first = checker[first]

        try:
            last = int(last)
        except:
            last = checker[last]

        print(first, last)

        a += int(str(first) + str(last))

    return a


main()
