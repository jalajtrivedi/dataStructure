class Solution:
    def reverseString(self, s: List[str]):
        stack =[]
        for ch in s:
            stack.append(ch)

        s.clear()

        while stack:
            ch = stack.pop()
            s.append(ch)
        return