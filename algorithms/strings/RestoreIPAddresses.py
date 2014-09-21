# Problem:
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# 
# Idea:
# Use Top-Down recursive!
# from the last charater of the str, for each charater:
# ether directly append it to the head or also append a '.'
# check several bad conditions.
class RestoreIPAddresses:
    result = []
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return self.result
        current = ""
        points = 3
        times = 1
        self.rec(s,len(s)-1,points,current,times)
        return self.result
    
    def rec(self,s,index,points,current,times):
        # check point number and currectness
        if points == 0 and len(s[0:index]) > 3:
            return
        # skip bad value
        if times == 3 and int(s[index])*100 + int(s[index+1])*10 + int(s[index+2]) > 255:
            return
        # end 
        if index == 0:
            if current.count('.') != 3:
                return
            current = s[index] + current
            self.result.append(current) 
            return

        if points > 0 and times <= 3:
            # apply '.' at this position
            self.rec(s,index-1, points-1,"." + s[index] + current, 1) 
        
        if times < 3:
            # not apply '.' at this position
            self.rec(s, index-1, points, s[index] + current, times+1)


print RestoreIPAddresses().restoreIpAddresses("111111111")

