import random
import time

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
# def remove_at(nums: list[int], index: int):
#     nums.pop(index)

# test = [1,2,3,4,5,6,7,8]
# remove_at(test,3)
# print(test)


# #查找元素
# def find(nums: list[int], target: int) -> int:
#     """在数组中查找指定元素"""
#     for i in range(0,len(nums)-1):
#         if nums[i] == target:
#             print(i)

# test = [1,2,3,4,5,6,7,8,9]
# find(test,9)


total = 50                      # 总量（单位数）
bar_width = 30                  # 进度条宽度
start = time.time()

for done in range(total + 1):
    now = time.time()
    elapsed = now - start

    # 速度：单位/秒（避免除0）
    speed = done / elapsed if elapsed > 0 else 0.0

    # 剩余时间 ETA：秒
    remaining = total - done
    eta = remaining / speed if speed > 0 else 0.0

    # 进度条
    progress = done / total if total else 1.0
    filled = int(progress * bar_width)
    bar = "#" * filled + "-" * (bar_width - filled)

    # 格式化时间 mm:ss
    eta_m, eta_s = divmod(int(eta), 60)

    print(
        f"\r[{bar}] {progress*100:6.2f}% "
        f"{done:>3d}/{total:<3d} "
        f"{speed:6.2f} it/s "
        f"ETA {eta_m:02d}:{eta_s:02d}",
        end="",
        flush=True,
    )

    time.sleep(0.05)

print()  # 换行