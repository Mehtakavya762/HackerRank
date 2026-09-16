def swap_case(s):
    result=[]
    
    for ch in s:
        if ch.isupper():
            result.append(ch.lower())
        elif ch.islower():
            result.append(ch.upper())      
        else:
            result.append(ch)
    return ''.join(result)
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna