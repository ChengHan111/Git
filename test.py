import pandas as pd

df = pd.read_csv("Iris_label_change.csv", nrows=51)

print(df.head(20))
print(df.sentiment.value_count())
