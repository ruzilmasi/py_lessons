import sys

with open('bakery.csv', 'a', encoding='utf-8') as f1:
    print(sys.argv[1], file=f1)
