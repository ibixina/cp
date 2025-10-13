numbers = map(int, input().split())



players_nums = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    0: 0,
}


laslt_winner = None

for i in numbers:
    units_digit = i % 10
    players_nums[units_digit] += 1
    if players_nums[units_digit] == 10:
        laslt_winner = units_digit

if laslt_winner == 0:
    laslt_winner = 10

print(laslt_winner)





