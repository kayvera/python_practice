
def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

def remove_duplicates(arr):
# index of the next non-duplicate element
    next_non_duplicate = 1

    i = 1
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
            i += 1

    return next_non_duplicate



