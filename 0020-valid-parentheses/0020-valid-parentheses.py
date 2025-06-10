class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        br_map={')': '(', '}': '{', ']': '['}
        for i in s:
            if i in br_map:
                top_element = stack.pop() if stack else '#'
                if br_map[i] != top_element:
                    return False
            else:
                stack.append(i)
        return not stack
        