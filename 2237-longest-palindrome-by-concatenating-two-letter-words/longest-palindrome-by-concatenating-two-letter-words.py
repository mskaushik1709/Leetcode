from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        center_used = False

        for word in count:
            rev = word[::-1]
            if word == rev:
                # For palindromic words like "gg", "cc"
                pairs = count[word] // 2
                length += pairs * 4  # each pair contributes 4
                if count[word] % 2 == 1:
                    center_used = True  # one word can be in the center
            else:
                # For non-palindromic words, match with their reverse
                if rev in count:
                    pairs = min(count[word], count[rev])
                    length += pairs * 4
                    # Mark both as used
                    count[word] = 0
                    count[rev] = 0

        if center_used:
            length += 2  # use one palindromic word in center

        return length
