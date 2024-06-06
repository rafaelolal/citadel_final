def stochastic_oscillator(prices, period=14):
    """Calculates the %K line of the Stochastic Oscillator."""
    k_values = []
    for i in range(period - 1, len(prices)):
        price_window = prices[i - period + 1: i + 1]
        highest_high = max(price_window)
        lowest_low = min(price_window)
        current_close = prices[i]
        k = ((current_close - lowest_low) / (highest_high - lowest_low)) * 100
        k_values.append(k)

    return k_values


def stochastic_daily_decisions(prices, k_values, overbought=80, oversold=20):
    """Generates trading signals based on Stochastic Oscillator %K values."""

    signals = [None] * (len(prices) - len(k_values))

    for i in range(len(k_values)):
        k = k_values[i]

        if k > overbought:
            signals.append("SELL")  # Sell signal (overbought)

        elif k < oversold:
            signals.append("BUY")  # Buy signal (oversold)

        else:
            signals.append("HOLD")  # Hold signal

    return signals
