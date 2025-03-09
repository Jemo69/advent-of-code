#https://adventofcode.com/2024/day/3
# import re

# pattern = r'mul\((\d{1,3},\d{1,3})\)'
# with open('input.txt', 'r') as file_in:
#     total = 0
#     for instruction in file_in:
#         found_pairs = re.findall(pattern, instruction)
#         for pair in found_pairs:
#             l, r = pair.split(',')
#             total += int(l) * int(r)

# print(total)
import re

pattern = r'mul\((\d{1,3},\d{1,3})\)'

def cal_sum(line):
    total = 0
    pairs = re.findall(pattern, line)
    print(pairs)
    for pair in pairs:
        x, y = pair.split(',')
        total += int(x) * int(y)
    return total

with open('input.txt', 'r') as file_in:
    total = 0
    instruction = file_in.read()
    print(instruction)
    instruction = re.sub(r"don't\(\).*?($|do\(\))", '', instruction, flags=re.DOTALL)
print(cal_sum(instruction))