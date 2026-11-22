def recurse(current_day, total_days):
    if current_day <= total_days:
        print(f"Day {current_day}")
        recurse(current_day + 1, total_days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recurse(1, days)
    print("Harvest time!")
