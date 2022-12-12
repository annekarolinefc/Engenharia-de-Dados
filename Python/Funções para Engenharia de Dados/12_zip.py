points_game1 = [50, 40, 60, 70, 80]
points_game2 = [76, 81, 53, 92, 67]

diffs = []

for x, y in zip(points_game1, points_game2):
    diffs.append(abs(x-y))

print(diffs)