def productExceptSelf(nums):
    length = len(nums)
    result = [1] * length
    left_product = 1
    for i in range(length):
        result[i] = left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]
print(productExceptSelf(nums2))