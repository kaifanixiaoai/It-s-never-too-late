# import random

# def random_access(num:list[int]) -> int:
#     """随机访问数组里的元素并且返回"""
#     random_index = random.randint(0, len(num) - 1)
#     random_number = num[random_index]
#     return random_number

# test = [1, 2, 3, 4, 5]
# print(random_access(test))


# def insert(nums: list[int], num: int, index: int):
#     """在数组的索引 index 处插入元素 num"""
#     nums.append(0)  # 先在数组末尾添加一个元素以扩展数组长度
#     for i in range(len(nums) - 1,index,-1):
#         nums[i] = nums[i - 1]
#     nums[index] = num

# test = [1, 2, 3, 4, 0, 0]
# insert(test, 80, 2)
# print(test)


# def remove(nums: list[int], index: int):
#     """删除索引 index 处的元素"""
#     if index < 0 or index >= len(nums):
#         raise IndexError("index out of range")
#     # 把索引 index 之后的所有元素向前移动一位
#     for i in range(index,len(nums)-1):
#         nums[i]=nums[i+1]
#     nums.pop

# test = [1,2,3,4,5,6,7,8]
# remove(test,10)
# print(test)

#极简写法
def remove_at(nums: list[int], index: int):
    nums.pop(index)

test = [1,2,3,4,5,6,7,8]
remove_at(test,3)
print(test)