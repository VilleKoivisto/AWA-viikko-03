"""
Testing Python Math-module, gets from user input:
- min, max, mean, median, mode

User input in format: num, num, num, num, etc
"""

import statistics


def get_values(user_input):
    values_in_temp_list = user_input.split(",") # temp list for str -> list comversion

    values_in_list = [] # new list init for stripping
        
    try:
        for value in values_in_temp_list:
            value = float(value.strip())

            values_in_list.append(value)

    except ValueError:
        raise ValueError

    v_min = min(values_in_list)
    v_max = max(values_in_list)
    v_mean = statistics.mean(values_in_list)
    v_median = find_median(values_in_list)
    v_mode = statistics.mode(values_in_list)

    return values_in_list, v_min, v_max, v_mean, v_median, v_mode


def find_median(values_list):
    count = len(values_list)
    index = count // 2

    if count % 2:
        return sorted(values_list)[index]
    
    return sum(sorted(values_list)[index - 1: index + 1]) / 2


if __name__ == "__main__":
    while True:
        print("Give numbers in format num,num,num,num,etc.")
        print("Empty line will terminate the script.")
        user_input = input(":")

        if user_input == "":
            break

        try:
            get_values(user_input)
            all_values, num_min, num_max, num_mean, num_median, num_mode = get_values(user_input)

        except ValueError:
            print("\nPlease give only integers or float values.\n")

        print(f"\nAll values: {all_values}")
        print(f"Min value: {num_min}")
        print(f"Max value: {num_max}")
        print(f"Mean: {num_mean}")
        print(f"Median: {num_median}")
        print(f"Mode: {num_mode}\n")