#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
if n % 2 != 0:
    print("Weird")     # These is odd

elif n % 2 == 0 and n in range (2,6):
    print("Not Weird") # It is even but in range (2,5)

elif n % 2 == 0 and n in range (6,21):
    print("Weird")     # It is even but in range (6,20)
    
elif n % 2 == 0 and n>20:
    print("Not Weird") # It is even but in range (n>20)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna