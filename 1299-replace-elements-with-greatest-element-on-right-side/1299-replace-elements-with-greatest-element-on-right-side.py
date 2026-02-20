class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        rightmax = -1
        arrayCopy = arr.copy()
        for i in range(n-1, -1, -1):
            arrayCopy[i] = rightmax
            rightmax = max(arr[i], rightmax)

        return arrayCopy