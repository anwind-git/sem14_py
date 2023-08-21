def bubble_sort(nums):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
    return nums