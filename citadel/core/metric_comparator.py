def max_profit(prices, dates, decisions):
    try:
        best_buy_index = decisions.index("BUY")
        max_profit_index = decisions.index("SELL", best_buy_index)
    except ValueError:
        raise ValueError(
            "Date range must contain at least one optimal buy and sell date")

    best_buy = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if decisions[i] is None:
            continue

        if decisions[i] == "BUY" and prices[i] < best_buy:
            best_buy = prices[i]
            best_buy_index = i
        elif decisions[i] == "SELL" and prices[i] - best_buy > max_profit:
            max_profit = prices[i] - best_buy
            max_profit_index = i

    return max_profit, dates[best_buy_index], dates[max_profit_index]
