class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def isPossible(self, possibleTotal, painters, wallList):
        currentTotal = 0

        for i in range(len(wallList)):
            if wallList[i] > possibleTotal:
                return False
            currentTotal += wallList[i]
            if (currentTotal > possibleTotal):
                currentTotal = wallList[i]
                painters -= 1

            if painters <= 0:
                return False

        if (currentTotal > possibleTotal):
            return False

        return True

    def paint(self, A, B, C):
        low = 0
        high = sum(C)
        mid = 0
        ans = 0
        while ( low <= high ):
            mid = low + (high - low) // 2
            if (self.isPossible(mid, A, C)):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1


        return (ans*B) % 10000003
