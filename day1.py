import numpy as np

measurements = np.genfromtxt('input1.txt', dtype=int)

# Part 1
print(np.sum(measurements[1:] > measurements[:-1]))

# Part 2
cs = measurements.cumsum()

# Add a zero term since the first rolling sum is correct without subtracting anything
offset_cs = cs.copy()
offset_cs[1:] = cs[:-1]
offset_cs[0] = 0

three_window = cs[2:] - offset_cs[:-2]
print(np.sum(three_window[1:] > three_window[:-1]))
