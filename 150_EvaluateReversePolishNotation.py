class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            else:
                latter = stack.pop()
                former = stack.pop()
                if tokens[i] == '+':
                    stack.append(former + latter) 
                elif tokens[i] == '-':
                    stack.append(former - latter) 
                elif tokens[i] == '*':
                    stack.append(former * latter)
                elif tokens[i] == '/':
                    stack.append(int(former / latter)) 
        # stack[0] is same as stack[-1] here. 
        #But stack[0] could help find the problem when there are at least two elements in the stack
        return stack[0]