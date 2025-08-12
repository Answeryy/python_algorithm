from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
          # 方法一
        temp = []
        length = len(pieces)
        for i in arr:
            for j in range(length):
                    
                if i in pieces[j]  and i not in temp:
                    # 将pieces[j]扩展到temp中
                    temp.extend(pieces[j])
                    
        if temp == arr:
            return True
        else:
            return False


"""
    已知一个目标数组arr,和一个二元数组pieces数组中的数均不相同
    判断目标数组是否能够由二元数组中的数组按任意次序链接而成
    如果可以链接构成目标数组,则返回True

"""
'''
    思考解题方式：
        方法1:
            遍历arr数组中的元素，遍历pieces数组，判断该元素在哪个二元数组中，
            如果遍历pieces发现元素均不在其中直接返回False
            如果遍历发现在其中一个二元数组中，则将二元数组扩展到 尝试数组中，
            遍历完成后比较 尝试数组是否等于目标target数组，如果相同则返回值True

                arr = [91,4,64,78]
                pieces = [[78],[4,64],[91]]
            # 这里出现一个问题4,64 存在于同一个子数组中
            91 
            
        方法2:
            遍历二元数组

'''
  

        
if __name__ == "__main__":
    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]

    res_obj = Solution()
    res = res_obj.canFormArray(arr=arr,pieces=pieces)
    print(res)
    