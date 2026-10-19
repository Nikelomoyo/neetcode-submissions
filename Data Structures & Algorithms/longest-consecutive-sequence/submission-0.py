class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if `num` is the beginning of a sequence,
            # meaning there is no number just below it.
            if num -1 not in num_set:
                current = num     # the number we're currently at
                length = 1          # length of the sequence so far
                
              # Walk upward as long as the next number exists
                while current +1 in num_set:
                    current +=1
                    length +=1

                 # Keep the best length seen
                longest = max(longest, length)

        return longest