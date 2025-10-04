from collections import Counter

s1, s2, s3, s4 = map(int, input().split())
nums = [s1, s2, s3, s4]

frequency = Counter(nums)

# Number of changes needed = total duplicates
changes = sum(count - 1 for count in frequency.values() if count > 1)

print(changes)
