from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        valid_numbers = set()
        
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue  # skip numbers with leading zero
            num = perm[0]*100 + perm[1]*10 + perm[2]
            if num % 2 == 0:
                valid_numbers.add(num)
        
        return sorted(valid_numbers)
