import sys
with open("input.txt") as fin:

    lines = fin.read().strip().split("\n")
    A, B, C = [int(lines[i].split(" ")[3]) for i in range(3)]
    program = list(map(int, lines[4].split(" ")[1].split(",")))


def run(program, A, B, C):
    ptr = 0

    def combo():
        x = program[ptr + 1]
        if x <= 3:
            return x
        if x == 4:
            return A
        if x == 5:
            return B
        if x == 6:
            return C

    def lit():
        return program[ptr + 1]

    while ptr < len(program):
        if ptr >= len(program):
            return

        opcode = program[ptr]

        # print(f"ptr: {ptr} ({A}, {B}, {C}), opcode: {opcode}, lit: {lit()}, combo: {combo()}")
        if ptr + 1 >= len(program) and opcode != 5: # added check to prevent index error for instructions needing arguments
            break

        if opcode == 0:
            res = A // pow(2, combo())
            A = res
        elif opcode == 1:
            res = B ^ lit()
            B = res
        elif opcode == 2:
            res = combo() % 8
            B = res
        elif opcode == 3:
            if A != 0:
                ptr = lit()
                continue # added continue to avoid ptr += 2 in this case
            else:
                ptr += 2
        elif opcode == 4:
            res = B ^ C
            B = res
        elif opcode == 5:
            res = combo() % 8
            yield res
        elif opcode == 6:
            res = A // pow(2, combo())
            B = res
        elif opcode == 7:
            res = A // pow(2, combo())
            C = res

        if opcode != 3: # only increment ptr by 2 if opcode is not 3 (jump)
            ptr += 2


ans = run(program, A, B, C)
print(",".join(map(str, list(ans))))

with open(sys.argv[1] if len(sys.argv) > 1 else "./day_17.in") as f:
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


def run(prog, rega, regb, regc):
    ip = 0
    out = []
    while ip < len(prog):
        if ip >= len(prog): # added check to prevent index error at the start of the loop
            break
        opcode = prog[ip]
        if ip + 1 >= len(prog) and opcode != 5: # added check to prevent index error for instructions needing arguments
            break
        oper = prog[ip + 1]
        combo = get_combo(oper, rega, regb, regc)
        match opcode:
            case 0:
                rega //= 2**combo
            case 1:
                regb ^= oper
            case 2:
                regb = combo % 8
            case 3:
                if rega:
                    if oper < len(prog): # added check to ensure jump target is within program bounds
                        ip = oper
                        continue # added continue to avoid ip += 2 in this case
                    else:
                        break # break loop if jump target is invalid
                else:
                    ip += 2
            case 4:
                regb ^= regc
            case 5:
                out.append(combo % 8)
            case 6:
                regb = rega // 2**combo
            case 7:
                regc = rega // 2**combo
        if opcode != 3: # only increment ip by 2 if opcode is not 3 (jump)
            ip += 2
    return out


print(",".join(map(str, run(prog, rega, regb, regc))))

rega = 0
j = 1
istart = 0
while j <= len(prog) and j >= 0:
    rega <<= 3
    for i in range(istart, 8):
        if prog[-j:] == run(prog, rega + i, regb, regc):
            break
    else:
        j -= 1
        rega >>= 3
        istart = rega % 8 + 1
        rega >>= 3
        continue
    j += 1
    rega += i
    istart = 0
print(rega)