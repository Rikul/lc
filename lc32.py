class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        wellformed = 0
        stk = []
        curr = 0

        for i,c in enumerate(s):

            if c == '(':
                stk.append(c)

            elif c == ')':
                if len(stk) > 0:
                    stk.pop()
                    curr += 2
                    if len(stk) == 0:
                        print(curr)

        return wellformed
            

if __name__ == "__main__":
    sol = Solution()
    result = sol.longestValidParentheses("((())(")
    print(f"result: {result}")