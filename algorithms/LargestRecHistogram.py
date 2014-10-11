class LargestRecHistogram:
    # @param height, a list of integer
    # @return an integer
    # def largestRectangleArea(self, height):

    # NOTE This solution is wrong and inefficient!!,
    def largestRectangleArea_Old(self, height):
        height.sort()
        maxmum = 0
        for i,x in enumerate(height):
            # len(height) - i is short for len(height)-1 - i + 1
            current = x * (len(height) - i)
            print current
            if current > maxmum:
                maxmum = current
        return maxmum

print LargestRecHistogram().largestRectangleArea([4,2])
