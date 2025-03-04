from alpha_vantage.timeseries import TimeSeries
import os

class PullStockData():
    API_KEY = os.environ.get("ALPHA_VANTAGE_KEY", None)

    @classmethod
    def get_stock_price(cls, stock_symbol: str) -> float:
        if cls.API_KEY == None:
            return 10.0
        else:
            return cls.get_price_from_alpha_vantage(stock_symbol)

    @classmethod
    def get_price_from_alpha_vantage(cls, stock_symbol) -> float:
        ts = TimeSeries(key=cls.API_KEY, output_format='json')
        data, _ = ts.get_intraday(symbol=stock_symbol, interval='1min', outputsize='compact')
        try:
            latest_time = list(data.keys())[1]  # The first key is 'Meta Data'
            latest_price = float(data[latest_time]['1. open'])
            return latest_price
        except KeyError:
            return 0.0

