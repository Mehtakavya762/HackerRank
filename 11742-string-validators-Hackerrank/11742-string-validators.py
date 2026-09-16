if __name__ == '__main__':
    s = input()
    
methods=[str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]

for method in methods:
    print(any(method(c)for c in s))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna