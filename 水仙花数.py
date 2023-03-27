"""
    一个三位数的 个位数的三次幂 + 十位数的三次幂 + 百位数的三次幂 等于这个数本身则称之为水仙花数
"""
for number in range(100,1000):
    a = number // 100
    b = (number % 100) // 10
    c = (number % 10)
    if a**3 + b**3 + c**3 == number:
        print(number)
    