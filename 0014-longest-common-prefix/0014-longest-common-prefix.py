class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        min_len = len(strs[0])
        if len(strs)==0 :
            return "";
        
        if len(strs)!=0:
            for i in range (1,len(strs)):
                min_len = min(min_len,len(strs[i]))
           # return min_len
        
        prefix = ""
        
        for i in range (0, min_len):
            for j in range (1, len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return prefix
                   # break
            prefix +=strs[0][i]   
            
        return prefix

            