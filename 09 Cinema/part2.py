import os

datafile = "input.txt"

def valid_rect(a, b, reds):
    
    # The rectangle is valid if there are no borders (between red tiles) within the rectangle
    # (excluding the rectangle's own border), assuming there are no zig-zagging borders without gaps.

    valid = True
    # Get rectangle limits
    rect_t = min(reds[a][1], reds[b][1])
    rect_b = max(reds[a][1], reds[b][1])
    rect_r = max(reds[a][0], reds[b][0])
    rect_l = min(reds[a][0], reds[b][0])
    # Thin rectangles are always valid:
    if rect_r - rect_l > 1 and rect_b - rect_t > 1:
        # Look for borders within the rectangle (excl. it's own border):
        red_count = len(reds)
        for n in range(red_count):
            tile1 = reds[n]
            tile2 = reds[(n+1) % red_count]
            # get border limits
            bord_t = min(tile1[1], tile2[1])
            bord_b = max(tile1[1], tile2[1])
            bord_r = max(tile1[0], tile2[0])
            bord_l = min(tile1[0], tile2[0])
            if not (bord_t >= rect_b or bord_b <= rect_t or bord_r <= rect_l or bord_l >= rect_r):
                valid = False
                break
    return valid

with open(os.path.dirname(os.path.abspath(__file__)) + "/" + datafile) as input:
    reds = [[int(x) for x in line.split(',')] for line in input]

largest = 0
for a in range(len(reds) - 1):
    for b in range(a + 1, len(reds)):
        area = (abs(reds[a][0] - reds[b][0]) + 1) * (abs(reds[a][1] - reds[b][1]) + 1)
        if area > largest and valid_rect(a, b, reds):
            largest = area

print('Result = ', largest)