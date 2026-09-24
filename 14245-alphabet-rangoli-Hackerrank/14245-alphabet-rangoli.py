def print_rangoli(size):
    # your code goes here
    width = 4 * size - 3
    for i in range(2 * size - 1):
        k = min(i, 2 * size - 2 - i)
        letters = [chr(ord('a') + (size - 1 - k) + abs(k - j))
                   for j in range(2 * k + 1)]
        mid = '-'.join(letters)
        print(mid.center(width, '-'))



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna