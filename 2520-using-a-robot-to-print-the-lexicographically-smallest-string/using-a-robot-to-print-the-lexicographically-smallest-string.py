class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        count = Counter(s) 
        t = []          
        result = []         
        min_char = 'a'      

        for ch in s:
            t.append(ch)
            count[ch] -= 1

            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            while t and t[-1] <= min_char:
                result.append(t.pop())

        while t:
            result.append(t.pop())

        return ''.join(result)
