class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lenthls=[]
        for word in words:
        	lenthls.append(len(word))
        while len(words) > 1:
	        word1 = words.index(max(lenthls))
	        words.pop(index(max(lenthls)))
	        word2 = words.index(max(lenthls))
	        for character in word1:
	        	if character in word2:
	        		continue
	        