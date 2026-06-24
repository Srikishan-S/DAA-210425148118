def INTERPOLATION_SEARCH(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
nums = [10, 20, 30, 40, 50]
target = 30
result = INTERPOLATION_SEARCH(nums, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")