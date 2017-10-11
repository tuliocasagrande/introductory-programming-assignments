class LargestNotation:
    def maxDigitsSum(self, N):
        return max([self.sumBase(N, i) for i in range(2, N)])

    def sumBase(self, n, b):
        s = 0
        while n:
            s += n % b
            n //= b
        return s
