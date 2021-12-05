def two_numbers_sum_to_2020(numbers):
    for n in numbers:
        for m in numbers:
            if n + m == 2020:
                return (n, m)


if __name__ == "__main__":
    numbers = [1721, 979, 366, 299, 675, 1456]
    print(two_numbers_sum_to_2020(numbers))