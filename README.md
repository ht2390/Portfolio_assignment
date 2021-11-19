# Portfolio_assignment

## Background:
This is a very basic assignment for you to practice **pandas** and **numpy**. The task is very simple: suppose you have **One Million** dollars account and you want to do some stock investments, The **orders-01.csv** files show all the trading records, and you need to **plot your account portfolio value** changes on a daily chart. Assume that you don't need to pay trading or commission fees and the portfolio will only change due to stock prices changes. Finally, you need to calculate the **average daily return** and **sharp ratio** for this portfolio.
 
## Requirement:
1. The template is **Main.py** file, you should write all your code inside it. When we run your main file, it should be bug-free and automatically generate the plot and print out all the statistics numbers. You can also add the SPX500 line in the plot as a comparison. 

2. Only use the stock prices data from **data** folder. Do not download the data from websites like Yahoo.

3. Only use python codes and libraries to generate this portfolio plot. The starting date and ending date for the plot should be **2011-01-01** and **2011-12-31**
And you only use **Adj close** price for all the tradings. 

4. In the **util.py** file, there are some build-up functions that could help you to do the assignment. 

5. Here are the equations for **average daily return** and **sharp ratio**:

daily_return = ( today's_portfolio_value / yesterday's_portfolio_value ) - 1 
( The first day doesn't have a valid daily return, you can get rid of the first value on daily_return vector)


average_daily_return = daily_return.mean()

sharpe_ratio = np.sqrt(252) * average_daily_return / daily_return.std()
