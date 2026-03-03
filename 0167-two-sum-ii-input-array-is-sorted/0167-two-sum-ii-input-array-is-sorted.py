class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mySet = set(numbers)

        for i in range(len(numbers)):
            if (target - numbers[i]) in mySet:
                if numbers[i] *2 ==target:
                    return [i+1, numbers[i+1:].index(numbers[i])+1+i+1]
                return [i+1, numbers.index(target - numbers[i])+1]