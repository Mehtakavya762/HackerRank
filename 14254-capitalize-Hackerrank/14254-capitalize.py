

# Complete the solve function below.
def solve(s):
  string=s.split(" ")
  result=[]
  for w in string:
    if w:
      result.append(w[:1].upper()+w[1:])
    else:
        result.append(w)
  return " ".join(result)
          


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna