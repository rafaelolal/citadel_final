from statistics import mean


def rsi(prices, period=14):
    deltas = [0] + [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    up = [0 if i < 0 else i for i in deltas]
    down = [0 if i > 0 else -i for i in deltas]
    up_ema = [0] * len(up)
    down_ema = [0] * len(down)
    rsis = [0] * len(up)
    a = 1 / period

    up_ema[period] = mean(up[:period+1])
    down_ema[period] = mean(down[:period+1])

    for i in range(period+1, len(up)):
        up_ema[i] = a * up[i] + (1 - a) * up_ema[i-1]
        down_ema[i] = a * down[i] + (1 - a) * down_ema[i-1]
        rs = up_ema[i] / down_ema[i] if down_ema[i] != 0 else 0
        rsis[i] = 100 - (100 / (1 + rs))

    return rsis


<<<<<<< HEAD
def daily_rsi_decisions(prices, rsis):
=======
def rsi_daily_decisions(prices, rsis):
>>>>>>> c3d67408cda330c6b1850ebe0fb3eed37120c0c8
    decisions = []
    for i in range(len(prices)):
        rsi_index = i - (len(prices) - len(rsis))
        if rsi_index < 0:
            decisions.append(None)

        else:
            if rsis[rsi_index] > 70:
                decisions.append("SELL")

            elif rsis[rsi_index] < 30:
                decisions.append("BUY")

            else:
                decisions.append("HOLD")

    return decisions
