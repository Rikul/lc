class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  # Initialize with -1 as a base index
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '(' onto stack
            else:  # char is ')'
                stack.pop()  # Pop the matching '('
                
                if not stack:  # If stack is empty, push current index as new base
                    stack.append(i)
                else:
                    # Calculate length of valid substring ending at current position
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
            
if __name__ == "__main__":
    sol = Solution()
    result = sol.longestValidParentheses("((())(")
    print(f"result: {result}")