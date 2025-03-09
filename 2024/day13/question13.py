import re

with open('input.txt', 'r') as f:
    machines = f.read().split('\n\n')

total = 0
for m in machines:
    lines = m.split('\n')
    a = tuple(map(int, re.findall(r'\d+', lines[0])))
    b = tuple(map(int, re.findall(r'\d+', lines[1])))
    prize = tuple(map(int, re.findall(r'\d+', lines[2])))

    # all possible presses of A
    max_a = min(prize[0] // a[0] + 1, prize[1] // a[1] + 1, 101)
    min_cost = float('inf')
    for a_presses in range(max_a + 1):
        x = a_presses * a[0]
        y = a_presses * a[1]
        if (prize[0] - x) % b[0] != 0:
            continue
        b_presses = (prize[0] - x) // b[0]
        if y + b_presses * b[1] != prize[1]:
            continue
        min_cost = min(min_cost, 3 * a_presses + b_presses)
    if min_cost < float('inf'):
        total += min_cost
print(total)
import re
import numpy as np

SHIFT = 10000000000000

with open('input.txt', 'r') as f:
    machines = f.read().split('\n\n')

total = 0
for m in machines:
    lines = m.split('\n')
    a = tuple(map(int, re.findall(r'\d+', lines[0])))
    b = tuple(map(int, re.findall(r'\d+', lines[1])))
    prize = tuple(map(int, re.findall(r'\d+', lines[2])))
    prize = (prize[0] + SHIFT, prize[1] + SHIFT)
    
    matrix = np.array([a, b], dtype=int).transpose()
    try:
        v = np.linalg.solve(matrix, prize)
        # to avoid errors due to round-off,
        # check if the integer version of v is a solution
        v[0] = round(v[0])
        v[1] = round(v[1])
        if not np.any(matrix@v - prize):
            total += int(3 * v[0] + v[1])
    except:
        print('Found a singular system')
        exit()
print(total)