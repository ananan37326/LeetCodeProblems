class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1,10))

        while queue:
            num = queue.popleft()
            if num > high:
                continue
            if low<=num<=high:
                res.append(num)
            
            one = num % 10

            if one < 9:
                queue.append(num*10 + (one+1))

        return res
        