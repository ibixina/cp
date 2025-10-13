import math
score_a = 0
score_b = 0

dest = (144, 84)

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

for _ in range(20):
    line = list(map(int, input().split()))
    team_a = []
    team_b = []

    print(len(line))
    lines = line[1:]
    turn = 0
    for i in range(0, len(lines), 2):
        print(i)
        j = (lines[i], lines[i + 1])
        if turn == 0:
            team_a.append(dist(dest, j))
        else:
            team_b.append(dist(dest, j))
        turn = 1 - turn

    sort_a = sorted(team_a)
    sort_b = sorted(team_b)

    print(sort_a)
    print(sort_b)

    if len(sort_a) == 0:
        score_b += len(sort_b)
        continue
    elif len(sort_b) == 0:
        score_a += len(sort_a)
        continue


    p, q = 0, 0

    if sort_a[0] < sort_b[0]:
        for g in sort_a:
            score_a += 1
    elif sort_a[0] > sort_b[0]:
        for g in sort_b:
            score_b += 1
print(score_a, score_b)






