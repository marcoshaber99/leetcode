class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for c in tokens:
            if c == "+":
                oper1 = stack.pop()
                oper2 = stack.pop()
                stack.append(oper1+oper2)
            elif c == "-":
                oper1 = stack.pop()
                oper2 = stack.pop()
                stack.append(oper2 - oper1)
            elif c == "/":
                oper1 = stack.pop()
                oper2 = stack.pop()
                stack.append(int(float(oper2) / oper1))

            elif c == "*":
                oper1 = stack.pop()
                oper2 = stack.pop()
                stack.append(oper1*oper2)

            else: 
                stack.append(int(c))
        return stack[0]
