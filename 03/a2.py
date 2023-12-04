import os
import re
checker = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

info = []

global sumPart


def main():
    with open(os.path.join(os.path.dirname(__file__), "example.txt"), "r") as file:
        # with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        content = file.read()

    build_index(content)
    # for i in info:
    #     print(i)
    # print(parse(content))
    check_part(info, content)


def check_part(info, content):

    rows = content.splitlines()

    grid = []

    for i, char in enumerate(rows):
        row = []
        for x in char:
            row.append(x)
        grid.append(row)

    print(grid)

    sumPart = 0

    is_part = False

    for num in info:
        # check vertical
        row = num['row']  # row of found number
        poss = num['pos']

        for pos in poss:
            if not grid[row][pos].isdigit() or not grid[row][pos] == '.':
                is_part = True
                sumPart += int(num['value'])
                break

        print(sumPart)

        # for i, char in enumerate(rows):
        #     if i == row:
        #         print("line", i)

        #         for index, c in enumerate(char):
        #             print(c)
        #             # if index in num['pos']:
        #             #     print(c)


def parse(content):
    lines = content.split('\n')
    sums = []

    for row, line in enumerate(lines):
        print("-----------")

        comps = list(line)

        for index, o in enumerate(comps):
            if not o in checker:
                print(f'checking {o} at x:{index+1} y:{row+1}')
                print("line:", row+1)

                sums.append(get_adjacent(index, row, line, lines))

    return sum(sums)


def get_adjacent(i, r, line, lines):
    comps = list(line)

    x = i
    y = r

    sums = []
    found = {
        'tl': 0,
        'up': 0,
        'tr': 0,
        'right': 0,
        'br': 0,
        'down': 0,
        'bl': 0,
        'left': 0,
    }

    print('\tCENTER is x:', x, 'y:', y)

    for item in info:
        # down
        if item['row'] == y+1 and x in item['pos']:
            print(f'found at down')
            print(f'found {item['value']} for x={x} and y={y+1} in {item["pos"]}')
            found['down'] = item['value']
        # up
        if item['row'] == y-1 and x in item['pos']:
            print(f'found at up')
            print(f'found {item['value']}  for x={x} and y={y-1} in {item["pos"]}')
            found['up'] = item['value']
        # right
        if item['row'] == y and x+1 in item['pos']:
            print(f'found at right')
            print(f'found {item['value']}  for x={x+1} and y={y} in {item["pos"]}')
            found['right'] = item['value']

        # left
        if item['row'] == y and x-1 in item['pos']:
            print(f'found at left')
            print(f'found {item['value']}  for x={x-1} and y={y} in {item["pos"]}')
            found['left'] = item['value']
        # br
        if item['row'] == y+1 and x+1 in item['pos']:
            print(f'found at br')
            print(f'found {item['value']}  for x={x+1} and y={y+1} in {item["pos"]}')
            found['br'] = item['value']
        # tr
        if item['row'] == y-1 and x+1 in item['pos']:
            print(f'found at tr')
            print(f'found {item['value']} for x={x+1} and y={y-1} in {item["pos"]}')
            found['tr'] = item['value']
        # bl
        if item['row'] == y+1 and x-1 in item['pos']:
            print(f'found at bl')
            print(f'found {item['value']}  for x={x-1} and y={y+1} in {item["pos"]}')
            found['bl'] = item['value']
        # tl
        if item['row'] == y-1 and x-1 in item['pos']:
            print(f'found at tl')
            print(f'found {item['value']}  for x={x-1} and y={y-1} in {item["pos"]}')
            found['tl'] = item['value']

    print(found)
    s = []
    for k in found:
        s.append(int(found[k]))

    if s[0] == s[1]:
        s[0] = 0
    if s[1] == s[2]:
        s[2] = 0
    if s[4] == s[5]:
        s[5] = 0
    if s[5] == s[6]:
        s[6] = 0

    print('-----------------------------------------------')

    return sum(s)


def build_index(full):
    full = full.split('\n')
    nums = []

    for pos, line in enumerate(full):
        line = re.sub(r'[^0-9]', ".", line)
        line_nums = line.split('.')

        for o, x in enumerate(line_nums):
            if not x == '':
                start = line.find(x)
                length = len(x)
                inds = [*range(start, start+length, 1)]
                out_line = {'row': pos, 'pos': inds, 'value': x}
                info.append(out_line)


main()
