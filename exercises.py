# 202. Happy Number ------ LEETCODE Write an algorithm to determine if a number n is happy.
#---------------------------------------------------------------------------------------------
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()  #to know every number we visit 
        
        while n not in visit:
            visit.add(n)   #add number to be visited
            n = self.SomeOfSquares(n)
            
            if n == 1:   
                return True
        return False
            
    def SomeOfSquares(self, n:int):
        output = 0
            
        while n:
            digit = n % 10
            digit = digit ** 2 
            output += digit
            n = n // 10
        return output

#---------------------------------------------------------------------------------------------
#66. Plus One - LEETCODE

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0:
            if (digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1 
        return [1] + digits
        
#---------------------------------------------------------------------------------------------
#22. Generate Parentheses - LEETCODE

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] #parenteses
        res = []  #list of valid parenteses combination 
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN +1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res

#--------------------------------------------------------------------------------------------- 
#98. Validate Binary Search Tree - LEETCODE >>>>> VALIDATE BINARY THREE USING DEPTH SEARCH (2 METHODS TRAINING AT ONCE)
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
        
            return(valid(node.left, left, node.val) and 
            valid(node.right, node.val, right))
    
        return valid(root, float("-inf"), float("+inf"))

#--------------------------------------------------------------------------------------------- 
        


            



