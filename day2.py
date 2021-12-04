# Part 1
pos = 0
depth = 0

with open('input2.txt') as file:
    for line in file:
        command, value = line.split()
        x = int(value)
        # handle forward, down, and up commands
        if command == 'forward':
            pos += x
        elif command == 'down':
            depth += x
        else:
            depth -= x

print(pos * depth)

# Part 2
pos = 0
depth = 0
aim = 0

with open('input2.txt') as file:
    for line in file:
        command, value = line.split()
        x = int(value)
        # handle forward, down, and up commands
        if command == 'forward':
            pos += x
            depth += aim * x
        elif command == 'down':
            aim += x
        else:
            aim -= x

print(pos * depth)
