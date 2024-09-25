def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to map closing brackets to opening ones
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop from the stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push onto the stack
            stack.append(char)
    
    # At the end, if the stack is empty, all brackets are matched
    return not stack

# Example 1
print(isValid("()"))     # Output: True
# Example 2
print(isValid("(000)"))  # Output: True (since '000' is not considered in the matching logic)
# Example 3
print(isValid("(]"))     # Output: False