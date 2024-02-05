from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # 遍历字符串数组words，依次取出字符串拼接判断是否与字符串s相同
        # 如果相同就返回True，遍历完成若不相等返回False
        length = len(words)
        temp_str = ''
        for i in range(length):
            temp_str += words[i]
            if  temp_str == s:
                return True 
        return False 