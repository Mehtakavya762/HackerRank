# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = map(int,input().split())

for i in range(1,a,2):
    
    print((".|."*i).center(b, "-"))
    
    
print("WELCOME".center(b, "-"))
    
for i in range(a-2,0,-2):
    
    print((".|."*i).center(b, "-"))    
    
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna