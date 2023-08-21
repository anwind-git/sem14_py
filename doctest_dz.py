def bubble_sort(nums):
    """
    Функция реализует алгоритм пузырьковой сортировки для сортировки списка чисел в порядке возрастания.
    >>> bubble_sort([5, 1, 3])
    [1, 3, 5]
    >>> bubble_sort([100, 50, 20])
    [20, 50, 100]
    >>> bubble_sort([7, 1, 3])
    [1, 3, 7]
    """

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)





