"""
 四叶玫瑰数：
    一个四位数的 千位数的四次方 + 百位数的四次方 + 十位数的四次方 = 这个数本身

"""
# 构造并遍历这四位数,筛选符合条件的数打印输出
for target_num in range(1000, 10000):
    a = target_num // 1000  # 9987 / 1000 = 9 ..987
    b = (target_num % 1000) // 100   # 9987 % 1000 =  987 // 100 = 9
    c= (target_num % 100) // 10
    d = target_num % 10
    if a**4 + b**4 +c**4 + d**4 == target_num:
        print(target_num)
# 1634 8208 9474


