def find_pair_with_sum(seq, Z):
    left = 0
    right = len(seq) - 1
    while left < right:
        if seq[left] + seq[right] == Z:
            return seq[left], seq[right], True
        elif seq[left] + seq[right] < Z:
            left += 1
        else:
            right -= 1
    return "not found", "not found", False

# Example usage
seq = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]
Z = 23
X, Y, found = find_pair_with_sum(seq, Z)
if found:
    print(f"X = {X}")
    print(f"Y = {Y}")
    print(f"X + Y = Z: {X + Y == Z}")
else:
    print("""X = not found"
"Y = not found"
"X + Y = Z: False""")

