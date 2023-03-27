 
# 如果a + b + c = 1000且a^2 + b^2 = c^2,求出所有的a、b、c可能的组合  
def fun():
    import time
    start_time = time.time()
    for a in range(0,1001):
        for b in range(0,1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(f"a:{a} b:{b} c:{c}")
    end_time = time.time()
    using_time = end_time - start_time
    print(using_time)
fun()   