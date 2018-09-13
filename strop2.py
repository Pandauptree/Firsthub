class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lenthls=[]
        multilen=0
        hashvalue=[]
        words.sort(key = lambda i:len(i), reverse=True)
        for i in range(len(words)):
            hashvalue.append(0)
            for j in set(words[i]):
                hashvalue[i] += 2**(ord(j)-ord('a'))
        max = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (hashvalue[i] & hashvalue[j]):
                    multilen=len(words[i])*len(words[j])
                    if multilen > max:
                        max = multilen
        return max