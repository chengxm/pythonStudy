prices = {
    'AAPL': 191.88,
    'GOOG': 1186.97,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89
}

# 用股票价格大于100元的股票构造一个新的字典

prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)