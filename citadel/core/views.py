from dotenv import load_dotenv
import os
import google.generativeai as genai
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

        metrics_functions = {
            'sma': simple_moving_averages,
            'ema': exponential_moving_averages,
            'wma': weighted_moving_averages,
            'rsi': rsi,
            'bollinger': bollinger_bands,
            'stochastic': stochastic_oscillator
        }

        decision_functions = {
            'sma': moving_average_daily_decisions,
            'ema': moving_average_daily_decisions,
            'wma': moving_average_daily_decisions,
            'rsi': rsi_daily_decisions,
            'bollinger': bollinger_bands_daily_decisions,
            'stochastic': stochastic_daily_decisions
        }

        data = {}
        for metric, function in metrics_functions.items():
            metric_values = function(prices)
            if metric == 'bollinger':
                metric_values = metric_values[0], metric_values[2]
            profit = max_profit(
                prices, dates, decision_functions[metric](prices, metric_values))
            data[metric] = profit

        draw_plot(data)

        return Response(data)


class LLMView(APIView):
    def get(self, request, format=None):
        text = request.query_params.get('text', None)

        load_dotenv()
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(text)
        response_text = response.text

        return Response(response_text)

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
