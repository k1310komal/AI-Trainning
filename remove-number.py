
nums = [3, 2, 3, 2]
val = 3
j = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[j] = nums[i]
        j += 1

print(j)
print(nums[:j])
