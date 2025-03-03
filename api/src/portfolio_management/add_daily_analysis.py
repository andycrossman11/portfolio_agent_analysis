from llm.llm_inference import LLM
from shared.database import DB_OPS, Position
from stock_market import PullStockData, StockData, convert_portfolio_data_to_string
from uuid import uuid4
from datetime import datetime

def add_daily_analysis(ch, method, properties, body) -> None:
    positions: list[Position] = DB_OPS.get_all_positions()
    stock_data_as_text: str = convert_positions_to_stock_data_text(positions)
    analysis: str = LLM.get_portfolio_analysis(stock_data_as_text)
    print(f"analysis: {analysis}")
    DB_OPS.create_daily_analysis(analysis, datetime.now())
    print("analysis added to")

def convert_positions_to_stock_data_text(positions: list[Position]) -> str:
    stock_data_list: list[StockData] = []
    for position in positions:
        print(position)
        today_price = PullStockData.get_stock_price(position.ticker)
        stock_data = StockData(ticker=position.ticker, buy_price=position.purchase_share_price, today_price=today_price, quantity=position.quantity)
        stock_data_list.append(stock_data)

    portfolio_data_as_text: str = convert_portfolio_data_to_string(stock_data_list)
    return portfolio_data_as_text

if __name__ == "__main__":
    positions: list[Position] = [
        Position(
            id=uuid4(),
            ticker="AAPL",
            quantity=10.5,
            total_purchase_price=1850.75,
            purchase_date=datetime.strptime("02-15-2024", "%m-%d-%Y")
        ),
        Position(
            id=uuid4(),
            ticker="MSFT",
            quantity=5.0,
            total_purchase_price=1875.50,
            purchase_date=datetime.strptime("01-10-2024", "%m-%d-%Y")
        ),
        Position(
            id=uuid4(),
            ticker="TSLA",
            quantity=3.2,
            total_purchase_price=780.00,
            purchase_date=datetime.strptime("12-05-2023", "%m-%d-%Y")
        ),
        Position(
            id=uuid4(),
            ticker="NVDA",
            quantity=8.0,
            total_purchase_price=3200.00,
            purchase_date=datetime.strptime("12-05-2023", "%m-%d-%Y")
        )
    ]
    add_daily_analysis(positions)