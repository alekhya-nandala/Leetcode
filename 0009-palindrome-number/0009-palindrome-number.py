class Solution:
    def isPalindrome(self, x: int) -> bool:
       if(abs(x)!= x):
          return False
       elif(str(x) == str(x)[::-1]):
           return True
       else:
          return False


        