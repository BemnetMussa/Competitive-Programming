def solve():
  """
  Solves a single test case for the B. Beautiful String problem.
  """
  try:
    n = int(input())
    s = input()

    # Iterate through all 2^n possible subsequences using a bitmask.
    # Each integer 'i' from 0 to 2^n - 1 represents a unique subsequence.
    for i in range(1 << n):
      p_chars = []
      p_indices = []
      x_chars = []

      # Construct the subsequence 'p' and the remaining string 'x'
      # based on the bits in the current mask 'i'.
      for j in range(n):
        # Check if the j-th bit is set in the mask 'i'
        if (i >> j) & 1:
          # If the bit is 1, add the character to 'p'
          p_chars.append(s[j])
          p_indices.append(j + 1) # Store the 1-based index
        else:
          # If the bit is 0, add the character to 'x'
          x_chars.append(s[j])

      p_str = "".join(p_chars)
      x_str = "".join(x_chars)

      # Condition 1: Check if 'p' is non-decreasing.
      # For a binary string, this means it doesn't contain "10".
      is_p_non_decreasing = '10' not in p_str

      # Condition 2: Check if 'x' is a palindrome.
      is_x_palindrome = (x_str == x_str[::-1])

      # If both conditions are met, we have found a solution.
      if is_p_non_decreasing and is_x_palindrome:
        print(len(p_indices))
        if p_indices:
          print(*p_indices)
        return

    # This part should theoretically not be reached as a solution is always possible.
    print(-1)

  except (IOError, ValueError):
    # Handle potential input errors gracefully
    return

# Read the number of test cases
try:
  t = int(input())
  for _ in range(t):
    solve()
except (IOError, ValueError):
  pass