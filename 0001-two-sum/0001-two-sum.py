class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       seen={}
       for i,num in enumerate (nums):
          sum=target-num

          if sum in seen:
            return[seen[sum],i] 

          seen[num]=i   

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna