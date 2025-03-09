import sys

def run(program, A, B, C):
    ptr = 0
    output = []

    while ptr < len(program):
        if ptr + 1 >= len(program):  # Ensure operand exists
            break
        opcode = program[ptr]
        operand = program[ptr + 1]

        def get_combo(x):
            if x <= 3:
                return x
            elif x == 4:
                return A
            elif x == 5:
                return B
            elif x == 6:
                return C

        combo = get_combo(operand)

        # Process opcode
        if opcode == 0:
            A = A // (2 ** combo)
            ptr += 2
        elif opcode == 1:
            B = B ^ operand
            ptr += 2
        elif opcode == 2:
            B = combo % 8
            ptr += 2
        elif opcode == 3:
            if A != 0:
                ptr = operand
            else:
                ptr += 2
        elif opcode == 4:
            B = B ^ C
            ptr += 2
        elif opcode == 5:
            output.append(combo % 8)
            ptr += 2
        elif opcode == 6:
            B = A // (2 ** combo)
            ptr += 2
        elif opcode == 7:
            C = A // (2 ** combo)
            ptr += 2
        else:
            ptr += 2  # Skip invalid opcode

    return output

# Read input for the first part
with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")
    A, B, C = [int(lines[i].split(" ")[3]) for i in range(3)]
    program_line = lines[4].split(" ")[1]
    program = list(map(int, program_line.split(",")))

# Execute and print the first result
ans = run(program, A, B, C)
print(",".join(map(str, ans)))

# Read input for the second part
input_file = sys.argv[1] if len(sys.argv) > 1 else "./day_17.in"
with open(input_file) as f:
    reg, prog = f.read().split("\n\n")

reg_lines = reg.splitlines()
rega = int(reg_lines[0].split(": ")[1])
regb = int(reg_lines[1].split(": ")[1])
regc = int(reg_lines[2].split(": ")[1])

prog = list(map(int, prog.split(": ")[1].split(",")))

# Execute and print the second result
result = run(prog, rega, regb, regc)
print(",".join(map(str, result)))

# Additional logic (unchanged)
rega = 0
j = 1
istart = 0
while j <= len(prog) and j >= 0:
    rega <<= 3
    for i in range(istart, 8):
        current_rega = rega + i
        if prog[-j:] == run(prog, current_rega, regb, regc):
            break
    else:
        j -= 1
        rega >>= 3
        istart = (rega % 8) + 1
        rega >>= 3
        continue
    j += 1
    rega += i
    istart = 0
print(rega)