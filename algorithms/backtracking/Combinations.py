# Problem
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# [
# [2,4],
# [3,4],
# [2,3],
# [1,2],
# [1,3],
# [1,4],
# ]
# NOTE k out of n is Combination (PaiLie), and 'Permutation' is ZuHe.
# Idea:
# Passed ont time!
# NOTE!NOTE! Question: Back Tracking?? no! DP? not sure!!!
# e.g.:
# 1,2,3,4 if we choose 1, we apply n=(2,3,4), k=1 as a sub-problem 
# then choose 2, then take n=(3,4), k=1 as a sub-problem (1 and 2 already be counted in the 1st condition).
# 3 can only together with 4 afterwards.
class Combinations:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.rec(1,n,k)
    def rec(self, start, end, k):
        if k == 1:
            # NOTE: return array of each value as a sub-array
            return [[x] for x in xrange(start,end+1)] 
        if k == end-start+1:
            # NOTE: return array of all value as a sub-array
            return [[x for x in xrange(start,end+1)]]
        result = []
        # NOTE end-k+2, e.g. n=4,k=2 then only loop on 1,2,3. 
        for i in xrange(start,end-k+2):
            values = self.rec(i+1, end, k-1)
            for x in values:
                result.append([i] + x)
        return result
            
print Combinations().combine(2,1)                

                
        
    
                    
