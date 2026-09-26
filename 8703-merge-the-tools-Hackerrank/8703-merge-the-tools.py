def merge_the_tools(string, k):
    # your code goes here
    slis=[string[i:i+k] for i in range(0,len(string),k)]
    for sub in slis:
        print("".join(dict.fromkeys(sub)))
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna