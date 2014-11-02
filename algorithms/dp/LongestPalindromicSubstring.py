class LongestPalindromicSubstring:
    # @return a string
    def longestPalindrome(self, s):
        board = [[False for x in s] for x in s]
        start = 0
        end = 0
        # i is start, j is end
        for j in xrange(len(s)):
            for i in xrange(j+1):
                if i == j:
                    board[i][j] = True
                elif j == i+1:
                    board[i][j] = s[i] == s[j]
                else:
                    board[i][j] = s[i] == s[j] and board[i+1][j-1] 
                if board[i][j]:
                    if j-i+1 > end-start:
                        start = i
                        end = j
        return s[start:end+1] 
        
print LongestPalindromicSubstring().longestPalindrome("lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges")
