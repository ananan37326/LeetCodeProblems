#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for op in tokens:
            if op == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif op == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b-a))
            elif op == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif op == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(op)
        
        return stack[0]
        
# @lc code=end

