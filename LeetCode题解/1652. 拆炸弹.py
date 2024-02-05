from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code) # 获取数组长度
        decrypt_num = [0]*n # 创建数组用来存储解密后的元素
        # 如何获得循环数组的下标
        """ 
            用取模的方式获得下标
            2%5 = 2
            7%5 = 2
            相当于实现了数组下标的循环
        """

        
        if k == 0:
            # 所有的数字均用0来替换
            return decrypt_num
        for i in range(n):
            if k > 0:
                # 将第i个数字用接下来的k个数字来代替
                # 不能使用切片来求和，只能使用+= 来求和
                for j in range(i+1,i+k+1):

                    decrypt_num[i] += code[j%n]

            elif k < 0:
                for j in range(i+k,i):
                
                    decrypt_num[i] += code[j%n]
        return decrypt_num


if __name__ == '__main__':
    code = [5,7,1,4]
    decrypt_obj = Solution()
    res = decrypt_obj.decrypt(code,3)
    print(res)

"""
    给定一个循环整数数组 code, 数组长度为 n
    指定一个秘钥K
    根据指定的方法替换 数组code中的每一个数,得到新的目标数组

    当数组code中的一个元素被替换时,其中的每个元素都会被替换
    如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
    如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
    如果 k == 0 ，将第 i 个数字用 0 替换。

    由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。
    
"""