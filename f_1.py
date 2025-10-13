import math
score_a = 0
score_b = 0

dest = (144, 84)
score_dist = 72.0 # can only score within this distance

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def read_line():
    line = []
    while not line:
        s = input().strip()
        if not s: 
            continue
        line = list(map(int, s.split()))
    return line

for _ in range(10):
    #read red line
    line = read_line()
    team_a = []
    lines = line[1:]
    for i in range(0, len(lines), 2):
        j = (lines[i], lines[i + 1])
        d = dist(dest, j)
        if d <= score_dist: #only keep them if they are in the house
            team_a.append(d)

    #yellow line
    line = list(map(int, input().split()))
    team_b = []
    lines = line[1:]
    turn = 0
    for i in range(0, len(lines), 2):
        j = (lines[i], lines[i + 1])
        d = dist(dest, j)
        if turn == 0:
            team_a.append(d)
        else:
            team_b.append(d)
        turn = 1 - turn

    #sort distances from destination
    sort_a = sorted(team_a)
    sort_b = sorted(team_b)

    if not sort_a and not sort_b: #not one in the house (no one scored
        continue
    if not sort_a: #only team b scored
        score_b += len(sort_b)
        continue
    if not sort_b: #only team a scored
        score_a += len(sort_a)
        continue

    if sort_a[0] < sort_b[0]: #team closest
        limit = sort_b[0]
        for d in sort_a:
            if d < limit:
                score_a += 1
            else:
                break
    elif sort_a[0] > sort_b[0]:
        limit = sort_a[0]
        for d in sort_b:
            if d < limit:
                score_b += 1
            else:
                break


print(score_a, score_b)   
