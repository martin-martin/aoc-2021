from pathlib import Path

data_dir = Path("/Users/martin/Documents/CodingNomads/community/aoc-2021/data")

depths = [int(d) for d in data_dir.joinpath("day1.txt").read_text().split("\n")]

WINDOW = 3  # Change window size here

count = 0

for index, depth in enumerate(depths):
    try:
        # breakpoint()
        sliding_window = [depths[index + n] for n in range(WINDOW)]
        sliding_window_next = [depths[index + n] for n in range(1, WINDOW + 1)]
        # breakpoint()
        # print(sliding_window)
    except IndexError:
        print(f"No more triplet values. Last item {depth=}, {index=}")
        break
    sliding_sum = sum(sliding_window)
    sliding_sum_next = sum(sliding_window_next)
    if sliding_sum < sliding_sum_next:
        count += 1

print(count)
