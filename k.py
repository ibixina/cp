import sys
queries = [(2,2), (2,4), (4,2)]

quarter = 3
for x, i in enumerate(queries):
    sys.stdout.flush()
    print(f"? {i[0]} {i[1]}")
    ans = input()
    if ans == "1":
        quarter = x
        break

# we know the quarter with 2 queries left

new_query_vec = [(0, -1), (1, 0)]

vectors = [(2,2), (2,4), (4,2), (4,4)]
vector = vectors[quarter]

sol = []
for i in new_query_vec:
    sys.stdout.flush()
    print(f"? {vector[0] + i[0]} {vector[1] + i[1]}")
    ans = input()
    sol.append(ans == "1")

if sol[0] and not sol[1]:
    solution = (vector[0] - 1, vector[1] - 1)
elif not sol[0] and sol[1]:
    solution = vector
elif sol[0] and sol[1]:
    solution = (vector[0], vector[1] -1)
else:
    solution = (vector[0] - 1, vector[1])

print(f"! {solution[0]} {solution[1]}")
