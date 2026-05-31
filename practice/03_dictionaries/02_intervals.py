intervals = [[2, 6],[1, 3],[15, 18],[8, 10]]
intervals.sort()
merged = [intervals[0]]
for current in intervals[1:]:
    last_added = merged[-1]
    if current[0] <= last_added[1]:
        last_added[1] = max(last_added[1], current[1])
    else:
        merged.append(current)
