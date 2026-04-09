import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# dataset = dataset

X = dataset[['Height']]
y = dataset['Weight']

model = LinearRegression()
model.fit(X, y)

dataset['Predicted_Weight'] = model.predict(X)

plt.figure(figsize=(8,5))
sns.scatterplot(x=X['Height'], y=y, color='blue', label='Actual Weight')
sns.lineplot(x=X['Height'], y=dataset['Predicted_Weight'], color='red', label='Regression Line')
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs. Weight Regression")
plt.legend()
plt.show()