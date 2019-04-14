def number_of_ways(no_of_steps):
    if no_of_steps == 0 or no_of_steps == 1:
        return 1
    else:
        return number_of_ways(no_of_steps-1) + number_of_ways(no_of_steps-2)

def number_of_ways_bottom_up(no_of_steps):
    if no_of_steps == 0 or no_of_steps == 1:
        return 1

    nums = [0 for x in range(no_of_steps)]
    nums[0] = 1
    nums[1] = 1
    for i in range(2, len(nums)):
        nums[i] = number_of_ways_bottom_up(nums[i-1]) + number_of_ways_bottom_up(nums[i-2])
    return nums[no_of_steps-1]

def num_ways_x(n, x):
    total = 0
    for i in x:
        if n-i >= 0:
            total += number_of_ways(n-i)
    return total

count = num_ways_x(3, [4])
print(count)


