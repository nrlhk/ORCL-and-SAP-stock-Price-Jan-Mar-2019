import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('ORCL.csv', index_col='Date', parse_dates=['Date'])  #index_col='Date'
df2 = pd.read_csv('SAP.csv', index_col='Date', parse_dates=['Date'])

df1JanMar = df1['01-01-2019': '31-03-2019']
# print(df1JanMar.head())
# print(df1JanMar['Close'].head())
df2JanMar = df2['01-01-2019': '31-03-2019']
# print(df2JanMar.head())
# print(df2JanMar['Close'].head())

plt.plot(df1JanMar.index, df1JanMar['Close'], 'c-', label='ORCL Close')
plt.plot(df2JanMar.index, df2JanMar['Close'], 'b-', label='SAP Close')
plt.title('Close Stock Price ORCL and SAP \n Jan-Mar 2019')
plt.grid()
plt.xlabel('Date')
plt.ylabel('USD')
plt.xticks(rotation=65)
plt.legend()
plt.subplots_adjust(
    left=0.09, bottom=0.25, right=0.97, top=0.88,
    wspace=.2, hspace=.2
)
plt.savefig('Stock Price SAP & ORCL Jan-Mar2019.jpg')  
plt.show()
