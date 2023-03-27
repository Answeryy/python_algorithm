# 将字符串 逆序输出 如'hello' 逆序输出为 'olleh'

s = 'hello'
# 第一种方法  切片逆索引
# s[start_index:end_index:step] 
# print(s[::-1])

# 利用循环然后逆序输出
str_list = []
for i in range(len(s)-1, -1, -1):
    str_list.append(s[i])

print(''.join(str_list))