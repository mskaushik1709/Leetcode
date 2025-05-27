class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Total sum of numbers from 1 to n
        total_sum = n * (n + 1) // 2
        
        # Count of numbers divisible by m from 1 to n
        count = n // m
        
        # Sum of numbers divisible by m using arithmetic progression
        divisible_sum = m * count * (count + 1) // 2
        
        # Sum of numbers not divisible by m
        non_divisible_sum = total_sum - divisible_sum
        
        return non_divisible_sum - divisible_sum
