def maximum_num(*numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest
print(maximum_num(-52, -3, -63, -23,))


#def max_num(*numbers):
 # return max(*numbers)

#print(max_num(-5, 3, 0, -25, 7, 10, -4, 30, -56, 16, 17, -21)) 