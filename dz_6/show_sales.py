import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) > 2:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
        for line in f.readlines()[start-1:stop]:
            print(line, end='')
    elif len(sys.argv) > 1:
        start = int(sys.argv[1])
        for line in f.readlines()[start-1:]:
            print(line, end='')
    elif len(sys.argv) > 0:
        print(f.read())
