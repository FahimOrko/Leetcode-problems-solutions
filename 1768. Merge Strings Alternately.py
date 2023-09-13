
# 1768. Merge Strings Alternately

class Solution:

    def __init__(self):
        pass

    def mergeAlternately(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.result = ""
        self.lenght  = 0
        self.bigger_word = ""

        if len(self.word1) <= len(self.word2):
            self.lenght = len(self.word1)
            self.bigger_word = self.word2
        else:
            self.lenght = len(self.word2)
            self.bigger_word = self.word1

        for  i in range(self.lenght):
            self.result += self.word1[i] + self.word2[i]
        
        self.result += self.bigger_word[self.lenght:]

        return self.result
    
    


w1 = Solution().mergeAlternately("abc","pqr")
print(w1)
        
