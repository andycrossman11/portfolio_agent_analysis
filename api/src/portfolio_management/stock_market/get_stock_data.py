from alpha_vantage.timeseries import TimeSeries

API_KEY = 'your_alpha_vantage_api_key'

def get_stock_price(stock_symbol: str) -> float:
    ts = TimeSeries(key=API_KEY, output_format='json')
    data, _ = ts.get_intraday(symbol=stock_symbol, interval='1min', outputsize='compact')
    try:
        latest_time = list(data.keys())[1]  # The first key is 'Meta Data'
        return float(data[latest_time]['1. open'])
    except KeyError:
        return 0.0

