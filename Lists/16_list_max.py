# Find max and min of a list without built-in functions

def max_min_manual(numbers):
    if not numbers:
        return None, None
    max_val = min_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

def max_min_sort(numbers):
    if not numbers:
        return None, None
    sorted_nums = sorted(numbers)
    return sorted_nums[-1], sorted_nums[0]

sample_list = [42, 7, 15, 3, 28, 9, 11]
print("\n=== Part 2: Max and Min in list ===")
print(f"List: {sample_list}")
max_m, min_m = max_min_manual(sample_list)
print(f"Manual loop -> Max: {max_m}, Min: {min_m}")
max_s, min_s = max_min_sort(sample_list)
print(f"Sorted method -> Max: {max_s}, Min: {min_s}")
