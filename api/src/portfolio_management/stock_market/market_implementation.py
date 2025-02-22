from .market_interface import MarketInterface

class MarketImplementation(MarketInterface):
    def __init__(self):
        print("MarketImplementation initialized")

    def get_stock_price(self, symbol: str) -> float:
        return 10.0