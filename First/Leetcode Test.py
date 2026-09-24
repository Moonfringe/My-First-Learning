class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        给定一个整数数组 nums 和一个整数目标值 target，
        请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
        你可以按任意顺序返回答案。(两次遍历，N（o²））
        :param nums:
        :param target:
        :return:
        """
        for i,item in enumerate(nums):
            for j in range(i+1,len(nums)):
                post = nums[j]
                if item + post == target:
                    return [i,j]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        给定一个整数数组 nums 和一个整数目标值 target，
        请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
        你可以按任意顺序返回答案.(哈希表做法N（o²））
        :param nums:
        :param target:
        :return:
        """
        cache = {}
        for i,item in enumerate(nums):
            cache[item] = i
        for i,item in enumerate(nums):
            other = target - item
            if other in cache and cache[other] != i:
                return[i,cache[other]]


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        给你一个整数 n ，返回一个字符串数组 answer（下标从 1 开始），其中：

        answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
        answer[i] == "Fizz" 如果 i 是 3 的倍数。
        answer[i] == "Buzz" 如果 i 是 5 的倍数。
        answer[i] == i （以字符串形式）如果上述条件全不满足。
        :param n:
        :return:
        """
        s = []
        for i in range(1,n+1):
            if i % 3 ==0 and i % 5 ==0:
                s.append("FizzBuzz")
            elif i % 3 ==0:
                s.append("Fizz")
            elif i % 5 ==0:
                s.append("Buzz")
            else:
                s.append(str(i))
        return s
sol = Solution()
print(sol.fizzBuzz(10))


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

        请返回 nums 的动态和。
        :param nums:
        :return:
        """
        num = []
        num_i = 0
        for i in range(len(nums)):
            num_i += nums[i]
            num.append(num_i)
        return num
sol = Solution()
print(sol.runningSum([1,2,3,4,5,6,7,8,9,10]))


