class Solution(object):
    def gcdOfStrings(self,str1,str2):

        def gcd(a:int ,b:int) -> int:
            while b:
                a,b = b ,a % b 
            return a
        
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len= gcd(len(str1),len(str2))

        return str1[:gcd_len]