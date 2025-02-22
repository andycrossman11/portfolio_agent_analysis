from abc import ABC, abstractmethod

class MarketInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_stock_price(self, symbol: str) -> float:
        pass