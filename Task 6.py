def maximum(num_1,*nums):
    max = 0
    for num_i in nums:
        if(num_i > max):
            max = num_i
    if(num_1 > max):
        return num_1
    else:
        return max

max = maximum(3,8,22,54,29,86,1,13,32)
print(max)