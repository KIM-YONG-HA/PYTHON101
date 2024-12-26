import sys

args = sys.argv[1:]
total = 0

for i in args:
    #print(type(i))
    total += int(i)

print(total)

