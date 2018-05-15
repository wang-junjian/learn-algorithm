def binary_search(list, value):
    low = 0
    high = len(list) - 1    # 这是索引，注意减1

    while low <= high:
        mid = int((low+high)/2) # int() 取整
        mid_value = list[mid]
        if value == mid_value:
            return mid
        elif value > mid_value:
            low = mid + 1   # 动起来
        else:
            high = mid - 1  # 动起来

    return None


list = [1, 3, 5, 7, 9]

# 测试查找每个值
[print(binary_search(list, value)) for value in list]
# 查找不存在的值
print(binary_search(list, 10))
