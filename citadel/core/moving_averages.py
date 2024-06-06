def simple_moving_averages(prices, period=20):
    assert len(
        prices) >= period, "Period is longer than price list"

    smas = []
    for i in range(period, len(prices)):
        sma = sum(prices[i-period:i])/period
        smas.append(sma)

    return smas


def exponential_moving_averages(prices, alpha=None, period=20):
    if alpha is None:
        alpha = 2/(period+1)

    assert len(
        prices) >= period, "Period is longer than price list"

    emas = []
    for i in range(period, len(prices)):
        if i == period:
            emas.append(sum(prices[:period])/period)
        else:
            emas.append((prices[i] - emas[-1]) * alpha + emas[-1])

    return emas


def weighted_moving_averages(prices, period=20):
    assert len(
        prices) >= period, "Period is longer than price list"

    wmas = []
    for i in range(period, len(prices)+1):
        n = i
        factor = n*(n+1)/2
        wma = sum([price*j/factor for j, price in enumerate(prices[:i])]
                  ) / sum([j/factor for j in range(1, i+1)])
        wmas.append(wma)

    return wmas


def moving_average_daily_decisions(prices, mas):
    decisions = []
    for i in range(len(prices)):
        mas_index = i - (len(prices) - len(mas))
        if mas_index < 0:
            decisions.append(None)

        else:
            if prices[i] > mas[mas_index]:
                decisions.append("SELL")

            else:
                decisions.append("BUY")

    return decisions


def moving_average_advice(prices, explain=False, client=False):
    period = int(input("Enter a period: "))
    period2 = int(
        input("Enter a shorter period to identify crossovers: "))

    smas = simple_moving_averages(prices, period)
    emas = exponential_moving_averages(prices, 2/(period+1), period)
    wmas = weighted_moving_averages(prices, period)

    smas2 = simple_moving_averages(prices, period2)
    emas2 = exponential_moving_averages(
        prices, 2/(period2+1), period2)
    wmas2 = weighted_moving_averages(prices, period2)

    advice = {"sma": {"decision": None, "explanation": None},
              "ema": {"decision": None, "explanation": None},
              "wma": {"decision": None, "explanation": None},
              "sma-crossover": {"decision": None, "explanation": None},
              "ema-crossover": {"decision": None, "explanation": None},
              "wma-crossover": {"decision": None, "explanation": None}}

    if smas[-1] > prices[-1]:
        advice["sma"]["decision"] = "SELL"
    else:
        advice["sma"]["decision"] = "BUY"

    if emas[-1] > prices[-1]:
        advice["ema"]["decision"] = "SELL"
    else:
        advice["ema"]["decision"] = "BUY"

    if wmas[-1] > prices[-1]:
        advice["wma"]["decision"] = "SELL"
    else:
        advice["wma"]["decision"] = "BUY"

    # crossovers are identified by comparing most recent rate of change
    if smas2[-1] - smas2[-2] > smas[-1] - smas[-2]:
        advice["sma-crossover"]["decision"] = "BUY"

    elif smas2[-1] - smas2[-2] < smas[-1] - smas[-2]:
        advice["sma-crossover"]["decision"] = "SELL"

    else:
        advice["sma-crossover"]["decision"] = "HOLD"

    if emas2[-1] - emas2[-2] > emas[-1] - emas[-2]:
        advice["ema-crossover"]["decision"] = "BUY"
    elif emas2[-1] - emas2[-2] < emas[-1] - emas[-2]:
        advice["ema-crossover"]["decision"] = "SELL"
    else:
        advice["ema-crossover"]["decision"] = "HOLD"

    if wmas2[-1] - wmas2[-2] > wmas[-1] - wmas[-2]:
        advice["wma-crossover"]["decision"] = "BUY"
    elif wmas2[-1] - wmas2[-2] < wmas[-1] - wmas[-2]:
        advice["wma-crossover"]["decision"] = "SELL"
    else:
        advice["wma-crossover"]["decision"] = "HOLD"

    return advice
