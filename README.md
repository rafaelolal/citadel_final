# Metric Comparator

A sophisticated financial analysis tool that compares various technical indicators to help make informed trading decisions.

## Project Overview

Metric Comparator is a web application built with Django and JavaScript that analyzes stock market data using multiple technical indicators. The application provides trading signals and visualizes comparative performance data to help users make informed investment decisions.

## Features

- **Multiple Technical Indicators**:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Weighted Moving Average (WMA)
  - Relative Strength Index (RSI)
  - Bollinger Bands
  - Stochastic Oscillator

- **Interactive Web Interface**:
  - Real-time stock data fetching
  - Date range selection
  - Interactive charts and visualizations
  - Trading view widget integration
  - AI-powered insights using Google's Gemini model

- **Data Analysis**:
  - Comparative analysis of different technical indicators
  - Maximum profit calculations
  - Buy/Sell/Hold signals
  - Historical price data visualization

## Usage

1. Access the application at `http://localhost:8000`
2. Enter a stock ticker symbol (e.g., "GME")
3. Select a date range for analysis
4. View the comparative analysis of different technical indicators
5. Check the AI-generated insights for deeper understanding

## Technical Stack

### Backend
- Django 5.0.6
- Python 3.12
- REST Framework
- Yahoo Finance API

### Frontend
- HTML/CSS/JavaScript
- Bootstrap 5
- TradingView widgets
- Matplotlib for visualization

### AI Integration
- Google Generative AI (Gemini 1.5)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/metric-comparator.git
cd metric-comparator
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
SECRET_KEY=your_django_secret_key
GOOGLE_API_KEY=your_google_api_key
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/core/max_profit/`: Returns maximum profit calculations based on technical indicators
- `/core/llm/`: Provides AI-generated insights about the analysis
