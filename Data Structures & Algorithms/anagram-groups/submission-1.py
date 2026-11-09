class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # act -> {'act': ["act"]}
        

        # for loop, make str key, counting appearance of each characters.
        # accumulate words into the dict.

        d = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            d[sorted_s].append(s)
        
        result = []
        for k in d:
            result.append(d[k])

        return result