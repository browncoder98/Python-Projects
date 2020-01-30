# Selection Sort:

def sort (nums):

    for i in range(5):
        minpos = i
        for j in range (i,6):
            if nums[j] < nums [minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos]= temp

        print(nums)

nums = [2,9,6,8,7,10]

sort(nums)

print(nums)