class Solution:

    def __init__(self):
        pass

    def gcdOfStrings(self, str1, str2):

        result = ""
        small = ""
        big = ""
        ans = ""

        
        if len(str1) > len(str2):
            small = str2
            big = str1
        else:
            small = str1
            big = str2
        
        if big == small:
            ans = small
        
        for i in range(len(small)):

            result += small[i]
            # print(result,len(small),i+1)
            # x = len(small)
            # y = int(x/(i+1))
            # z = i+1
            # print(result * y)

            # print(result * (len(small)//(i+1)))

            # if small * (i+1) == big:
            #     return small

            if result * (len(small)//(i+1)) == small and result * (len(big)//len(result)) == big:
                ans = result

        return ans
                
print(Solution().gcdOfStrings("ABCABC","ABC"))