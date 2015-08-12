# Create two new columns in a dataframe from pre-existing columns
def calculate(x):
  return x*2, x*3

df = DataFrame({'a': [1,2,3], 'b': [2,3,4]})

df["A1"], df["A2"] = zip(*df["a"].map(calculate))
