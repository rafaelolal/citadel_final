import datetime
from django.shortcuts import render
from yahoofinancials import YahooFinancials
from .moving_averages import simple_moving_averages, exponential_moving_averages, weighted_moving_averages, moving_average_daily_decisions
from .rsi import rsi, rsi_daily_decisions
from .metric_comparator import max_profit
from .bollinger_bands import bollinger_bands, bollinger_bands_daily_decisions
from rest_framework.views import APIView
from rest_framework.response import Response
from .draw_plot import draw_plot
from .stochastic_oscillator import stochastic_oscillator, stochastic_daily_decisions

# Create your views here.

metrics = {
    'simple_moving_average': simple_moving_averages,
    'exponential_moving_averages': exponential_moving_averages,
    'weighted_moving_averages': weighted_moving_averages,
    'rsi': rsi,
}

# Define a list of parameter groups
# parameter_groups = [
#     {
#         'name': 'moving_average_crossover',
#         'parameters': {
#             'long_period': None,
#             'short_period': None,
#         }
#     },
#     {
#         'name': 'boolean_param',
#         'parameters': {
#             'boolean_param': None,
#         }
#     },
#     # Add more parameter groups as needed
# ]


def convert_epoch_to_date(epoch_seconds):
    date = datetime.datetime.fromtimestamp(epoch_seconds)
    return date.strftime('%Y-%m-%d')


class MaxProfitView(APIView):
    def get(self, request, format=None):
        ticker_symbol = request.query_params.get('ticker', None)
        ticker = YahooFinancials(ticker_symbol)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        data = ticker.get_historical_price_data(
            start,
            end,
            "daily")
        prices = [day["close"] for day in data[ticker_symbol]["prices"]]
        dates = [day["formatted_date"]
                 for day in data[ticker_symbol]["prices"]]

        smas = simple_moving_averages(prices)
        emas = exponential_moving_averages(prices)
        wmas = weighted_moving_averages(prices)
        rsis = rsi(prices)
        bollingers = bollinger_bands(prices)
        stochastics = stochastic_oscillator(prices)

        sma_profit = max_profit(
            prices, dates, moving_average_daily_decisions(prices, smas))
        ema_profit = max_profit(
            prices, dates, moving_average_daily_decisions(prices, emas))
        wma_profit = max_profit(
            prices, dates, moving_average_daily_decisions(prices, wmas))
        rsi_profit = max_profit(
            prices, dates, rsi_daily_decisions(prices, rsis))
        bollinger_profit = max_profit(prices, dates, bollinger_bands_daily_decisions(
            prices, bollingers[0], bollingers[2]))
        stochastic_profit = max_profit(
            prices, dates, stochastic_daily_decisions(prices, stochastics))

        data = {
            'sma': sma_profit,
            'ema': ema_profit,
            'wma': wma_profit,
            'rsi': rsi_profit,
            'bollinger': bollinger_profit,
            'stochastic': stochastic_profit,
        }

        draw_plot(data)

        return Response(data)


# class StockDataView(APIView):
#     def get(self, request, format=None):
#         ticker = request.query_params.get('ticker', None)

#         if ticker is not None:
#             stock_data = fetch_stock_data(ticker)

#             # Initialize an empty dictionary to store the calculation results
#             calculation_results = {}

#             # Iterate over the parameter groups
#             for group in parameter_groups:
#                 # Check if all parameters in the group are provided in the request
#                 if all(param in request.query_params for param in group['parameters']):
#                     # Perform the calculation and add the result to the response
#                     calculation_results[group['name']] = metrics[group['name']](
#                         stock_data, **{param: request.query_params[param] for param in group['parameters']})

#             return Response({
#                 'ticker': ticker,
#                 'data': stock_data,
#                 'calculations': calculation_results
#             })

#         return Response({'error': 'No ticker provided'}, status=400)
