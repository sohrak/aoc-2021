# Part 1
with open('input3.txt') as file:
    lines = file.readlines()


def calc_gamma_epsilon(values):
    first_line = True
    for line in values:
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
        if one >= zero:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return gamma, epsilon


gamma, epsilon = calc_gamma_epsilon(lines)
gamma_val = int(gamma, 2)
epsilon_val = int(epsilon, 2)
print(gamma_val * epsilon_val)

# Part 2
oxygen = lines.copy()
co2 = lines.copy()

# reuse gamma and epsilon from above (initally)
for i in range(len(gamma)):
    oxygen = [x for x in oxygen if x[i] == gamma[i]]
    if len(oxygen) == 1:
        break
    gamma, _ = calc_gamma_epsilon(oxygen)

for i in range(len(epsilon)):
    co2 = [x for x in co2 if x[i] == epsilon[i]]
    if len(co2) == 1:
        break
    _, epsilon = calc_gamma_epsilon(co2)

oxygen_val = int(oxygen[0], 2)
co2_val = int(co2[0], 2)
print(oxygen_val * co2_val)
