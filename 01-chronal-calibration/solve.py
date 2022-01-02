import fileinput


def parse_input(file):
    counter = 0
    seen = [0]
    operations = []
    for line in file:
        if line[0] == '+':
            add = int(line[1:].strip())
        else:
            add = 0 - int(line[1:].strip())
        counter += add
        operations.append(add)
        seen.append(counter)
    print(f"Part 1: {counter}")
    while True:
        for add in operations:
            counter += add
            if counter in seen:
                return counter


calculator = parse_input(fileinput.input())
print(f"Part 2: {calculator}")
