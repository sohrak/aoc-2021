# Part 1
with open('input3.txt') as file:
    first_line = True
    for line in file:
        if first_line:
            first_line = False
            length = len(line)
            if line.endswith('\n'):
                length -= 1
            zero_count = [0] * length
            one_count = [0] * length

        for i, bit in enumerate(line):
            if bit == '0':
                zero_count[i] += 1
            elif bit == '1':
                one_count[i] += 1

gamma = ''
epsilon = ''
for zero, one in zip(zero_count, one_count):
    if one > zero:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma_val = int(gamma, 2)
epsilon_val = int(epsilon, 2)
print(gamma_val * epsilon_val)
