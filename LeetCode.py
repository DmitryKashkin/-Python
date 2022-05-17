def removeDuplicates(nums):
    i = 0
    lenght = len(nums) - 1
    while i < lenght:
        if nums[i] == nums[i + 1]:
            del nums[i]
            lenght -= 1
        else:
            i += 1
    return lenght + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(nums)
print(removeDuplicates(nums))
print(nums)
