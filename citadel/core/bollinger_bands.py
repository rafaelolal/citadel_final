def bollinger_bands(prices, period=20, std_dev_multiplier=2):
    """
    Calculates Bollinger Bands for a given price series using basic Python lists.

    Args:
        prices (list): The closing prices of the asset.
        period (int, optional): The period for calculating the moving average and standard deviation. Defaults to 20.
        std_dev_multiplier (float, optional): The multiplier for the standard deviation. Defaults to 2.

    Returns:
        tuple: A tuple containing lists of upper band, middle band, and lower band values.
    """

    upper_band = []
    middle_band = []
    lower_band = []

    for i in range(period - 1, len(prices)):
        price_window = prices[i - period + 1: i + 1]

        # Calculate moving average
        sma = sum(price_window) / period

        # Calculate standard deviation
        squared_diffs = [(price - sma) ** 2 for price in price_window]
        std_dev = (sum(squared_diffs) / period) ** 0.5

        # Calculate bands
        upper = sma + std_dev * std_dev_multiplier
        lower = sma - std_dev * std_dev_multiplier

        upper_band.append(upper)
        middle_band.append(sma)
        lower_band.append(lower)

    return upper_band, middle_band, lower_band


def bollinger_bands_daily_decisions(prices, bands):
    """
    Generates buy, sell, or hold signals based on Bollinger Bands.

    Args:
        prices (list): The closing prices of the asset.
        upper_band (list): The upper Bollinger Band values.
        lower_band (list): The lower Bollinger Band values.

    Returns:
        list: A list with buy (1), sell (-1), or hold (0) signals.
    """

    upper_band, lower_band = bands

    signals = [None] * (len(prices) - len(upper_band))

    for i in range(len(upper_band)):
        if prices[i + len(prices) - len(upper_band)] > upper_band[i]:
            signals.append("SELL")  # Sell signal
        elif prices[i + len(prices) - len(upper_band)] < lower_band[i]:
            signals.append("BUY")  # Buy signal
        else:
            signals.append("HOLD")  # Hold signal

    return signals
