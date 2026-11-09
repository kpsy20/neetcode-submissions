class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0


        char_set = set()
        max_len = 0
        

        # zxyzxyz
        #  l
        #     r
        # char_set = x, y, z
        # max_len = 3
        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
            
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                
            max_len = max(max_len, r-l)
        return max_len