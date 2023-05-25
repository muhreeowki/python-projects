
def naive_search(nums, target):
    # example nums = [1, 3, 10, 12, 20, 32]
    # example target = 10
    # example output = 2
    for i in range(len(nums) - 1):
        if nums[i] == target: return i
    return -1

def bisearch(nums, target, left=None, right=None):
    if left == None:
        left = 0
    if right == None:
        right = len(nums) - 1

    if right < left:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target: return mid
    elif target < nums[mid]: return bisearch(nums, target, left, mid - 1)
    else: return bisearch(nums, target, mid + 1, right)


if __name__ == '__main__':
    nums = [1, 3, 5, 10, 12]
    target = 10

    print(naive_search(nums, target))
    print(bisearch(nums, target))