import numpy as np
from scipy.ndimage import generic_filter

with open("input.txt") as f:
    lines = [list(x.strip().replace("A", "3").replace("M", "2").replace("S", "4").replace("X", "1")) for x in f]

img = np.array(lines).astype("uint8")

def find_part1(arr):
    arr = np.reshape(arr, (7,7))
    # If middle character is "X", then we check in all directions
    if arr[3][3] == 1:
        pos = [
            (arr[3][4], arr[3][5], arr[3][6]),
            (arr[3][2], arr[3][1], arr[3][0]),
            (arr[4][3], arr[5][3], arr[6][3]),
            (arr[2][3], arr[1][3], arr[0][3]),
            (arr[4][4], arr[5][5], arr[6][6]),
            (arr[2][2], arr[1][1], arr[0][0]),
            (arr[4][2], arr[5][1], arr[6][0]),
            (arr[2][4], arr[1][5], arr[0][6])
        ]
        return sum(p == (2,3,4) for p in pos)
    return 0

res = generic_filter(img, find_part1, size=7, mode="constant", cval=0)
print(res)
print(np.sum(res))

def find_part2(arr):
    # If middle character is "A", there are four possible crosses
    # M . S     S . M     M . M     S . S
    # . A .     . A .     . A .     . A .
    # M . S     S . M     S . S     M . M
    if arr[4] == 3:
        return any([
            arr[0] == 2 and arr[2] == 4 and arr[6] == 2 and arr[8] == 4,
            arr[0] == 4 and arr[2] == 2 and arr[6] == 4 and arr[8] == 2,
            arr[0] == 2 and arr[2] == 2 and arr[6] == 4 and arr[8] == 4,
            arr[0] == 4 and arr[2] == 4 and arr[6] == 2 and arr[8] == 2,
        ])
    return 0 

res = generic_filter(img, find_part2, size=3, mode="constant", cval=0)
print(res)
print(np.sum(res))
