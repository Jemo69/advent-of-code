import sys

# First make sure we properly read the input file
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    reg, prog = f.read().split("\n\n")

prog = list(map(int, prog.split(": ")[1].split(",")))
rega, regb, regc = (int(line.split(": ")[1]) for line in reg.splitlines())


def get_combo(oper, rega, regb, regc):
    if 0 <= oper <= 3:
        return oper
    if oper == 4:
        return rega
    if oper == 5:
        return regb
    if oper == 6:
        return regc
    return 0  # Default case to avoid undefined behavior


def run(prog, rega, regb, regc):
    ip = 0
    out = []
    while ip < len(prog) - 1:  # Need at least 2 elements for each instruction
        # Check if we have enough space for operation and argument
        if ip + 1 >= len(prog):
            break

        oper = prog[ip + 1]
        combo = get_combo(oper, rega, regb, regc)

        match prog[ip]:
            case 0:
                rega //= 2**combo
            case 1:
                regb ^= oper
            case 2:
                regb = combo % 8
            case 3:
                if rega:
                    ip = oper
                    continue
            case 4:
                regb ^= regc
            case 5:
                out.append(combo % 8)
            case 6:
                regb = rega // 2**combo
            case 7:
                regc = rega // 2**combo
        ip += 2
    return out


# Get the output from the run function
output = run(prog, rega, regb, regc)
print(",".join(map(str, output)))

# Fix the final part with proper bounds checking
rega = 0
j = 1
istart = 0
while j <= len(prog) and j > 0:  # Fixed condition to avoid negative indices
    rega <<= 3
    found_match = False

    for i in range(istart, 8):
        # Make sure we don't access invalid indices
        if j <= len(prog):
            expected_output = prog[-j:] if j > 0 else []
            actual_output = run(prog, rega + i, regb, regc)

            # Only compare the appropriate lengths
            if expected_output == actual_output[: len(expected_output)]:
                found_match = True
                break

    if not found_match:
        j -= 1
        if j > 0:  # Make sure j is still positive before bit shifting
            rega >>= 3
            istart = rega % 8 + 1
            rega >>= 3
        continue

    j += 1
    rega += i
    istart = 0

print(rega)
