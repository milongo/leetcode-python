"""Stack problems"""


def is_valid(s: str) -> bool:
    """Compute if string is valid parenthesis"""
    pairs = {")": "(", "}": "{", "]": "["}

    stack = []

    for char in s:
        if char in pairs:  # char is a closer
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack
