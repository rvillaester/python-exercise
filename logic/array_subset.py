# find how many subsets in a given array that sums up to total
def count_sets(arr, total):
    return recurse(arr, total, len(arr) - 1)
def recurse(arr, total, index):
    if total == 0: return 1
    elif total < 0: return 0
    elif index < 0: return 0
    elif total < arr[index]:
        return recurse(arr, total, index - 1)
    else:
        return recurse(arr, total - arr[index], index - 1) + recurse(arr, total, index - 1)

count = count_sets([2, 4, 6, 10], 14)
print(count)