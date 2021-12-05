from pathlib import Path

data_dir = Path("/Users/martin/Documents/CodingNomads/community/aoc-2021/data")

depths = [int(d) for d in data_dir.joinpath("day1.txt").read_text().split("\n")]
print(depths)

count = 0

for index, depth in enumerate(depths):
    if (index > 0) and (depth > depths[index - 1]):
        count += 1

print(count)