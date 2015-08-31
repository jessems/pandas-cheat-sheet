# Create two new columns in a dataframe from pre-existing columns
def calculate(x):
  return x*2, x*3

df = DataFrame({'a': [1,2,3], 'b': [2,3,4]})

df["A1"], df["A2"] = zip(*df["a"].map(calculate))

# Convert string to int while accounting for non-convertible strings
# This will use 0 in the case when you provide any value that Python considers False
int(value or 0)

# Categorize an array of numerical values:
df = pd.DataFrame([1921,1924,1941,1956,1965,1970,1980,1992,1999,2014])
year_category_labels = ['pre-war', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', 'modern cars']
pd.cut(df.year, [0,1939,1946,1950,1960,1970,1980,1990,2015], labels=year_labels)

# Creating a DataFrame. (Put the dict in a list)
mydata = [{'subid' : 'B14-111', 'age': 75, 'fdg':1.78},
              {'subid' : 'B14-112', 'age': 22, 'fdg':1.56},]
df = pandas.DataFrame(mydata)
