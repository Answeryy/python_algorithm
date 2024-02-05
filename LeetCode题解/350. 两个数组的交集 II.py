class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 将两数组排序
        nums1.sort()
        nums2.sort()
        # 创建一个空数组用来存储交集元素
        ans = []
        # 创建两个分别指向两数组头部的指针
        i = j = 0
        len(nums1)
        len(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans