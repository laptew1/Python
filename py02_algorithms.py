nums = [77, 1, 2, 3, 4, 0, 1234]

# Найти минимум
min_num = nums[0]
for x in nums:
    if x < min_num:
        min_num = x
        
print(min_num)

# Написать код, который выведет сумму nums (12:16)
summa = 0
for x in nums:
    summa += x
print(summa)    

nums1 = [77, 7, 1, 2, 66, 5]
nums2 = [777, 66, 5, 4]

# Срвенение двух список - асимптотика O(n^2)
for x1 in nums1:
    for x2 in nums2:
        if x1 == x2:
            print(x1)

# Сравнение двух список - асимптотика O(n log n)
combined = nums1 + nums2 # O(n)
# print(combined)
combined = sorted(combined) # O(n log n)
# print(combined)
for i in range(0, len(combined) - 1): # O(n)
    if combined[i] == combined[i + 1]: # O(1)
        print(i, combined[i])
