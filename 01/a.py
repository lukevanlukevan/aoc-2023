import os
import re
from word2number import w2n


def main():
    with open(os.path.join(os.path.dirname(__file__), "example.txt"), "r") as file:
        content = file.read()

    print(parse(content))


def parse(content):
    lines = content.splitlines()
    a = 0
    for i, line in enumerate(lines):

        strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        finds = []
        for num in strings:
            if num in line:
                finds.append(num)

        nums = re.findall(r'\d', line)

        first = ''
        last = ''

        try:
            if line.find(nums[0]) > line.find(finds[0]):
                first = finds[0]
        except:
            first = nums[0]

        try:
            if line.find(nums[-1]) > line.find(finds[-1]):
                last = finds[0]
        except:
            last = nums[0]

        print(first, last)

        st = nums[0] + nums[-1]
        a += int(st)

    return a


main()
