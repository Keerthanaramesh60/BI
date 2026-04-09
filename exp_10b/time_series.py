import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

df=pd.read_csv(r"C:\Users\user1\Downloads\time_series_sales_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

decomposition = seasonal_decompose(df['Sales'], model='additive', period=30)
df['Trend'] = decomposition.trend
df['Seasonality'] = decomposition.seasonal
df['Residual'] = decomposition.resid

plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(df.index, df['Sales'], label='Original Sales', color='blue')
plt.title('Original Sales Data')
plt.legend()
plt.subplot(4, 1, 2)
plt.plot(df.index, df['Trend'], label='Trend', color='red')
plt.title('Trend Component')
plt.legend()
plt.subplot(4, 1, 3)
plt.plot(df.index, df['Seasonality'], label='Seasonality', color='green')
plt.title('Seasonality Component')
plt.legend()
plt.subplot(4, 1, 4)
plt.plot(df.index, df['Residual'], label='Residual', color='purple')
plt.title('Residual Component')
plt.legend()
plt.tight_layout()
plt.show()