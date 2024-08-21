def min(*numbers):
    min_value=numbers[0]
    max_value=numbers[0]
    for number in numbers:
        if min_value>number:
            min_value=number
        if max_value<number:
            max_value=number
    return min_value,max_value
result=min(1,3,1346,34,3,345)
print(result)
a,b=min(35,643,85,153,850)
print("최솟값:",a, "최댓값:",b)
