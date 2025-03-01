import os
import json
import ollama
from pydantic import BaseModel

class StockData(BaseModel):
    ticker: str
    buy_price: float
    today_price: float
    quantity: int

class LLM():
    host = os.getenv("OLLAMA_HOST", "localhost")

    ollama.api_base = f"http://{host}:11434"

    @staticmethod
    def get_portfolio_analysis(portfolio_data: list[StockData]) -> str:
        return LLM._get_analysis_from_llm(portfolio_data)
    
    @staticmethod
    def _get_analysis_from_llm(portfolio_data: list[StockData]) -> str:
        llm_to_use = os.environ.get('LLM', None)
        print(llm_to_use)
        if llm_to_use is None:
            return f"ANALYSIS: {convert_portfolio_data_to_string(portfolio_data)}"
        elif llm_to_use == 'LLAMA3.2':
            print("here")
            return LLM._get_ollama_analysis(portfolio_data)
        
    @staticmethod
    def _get_ollama_analysis(portfolio_data: list[StockData]) -> str:
        pretty_portfolio_data = convert_portfolio_data_to_string(portfolio_data)
        prompt: str = f"""
        You are a financial advisor and you have been given the task of analyzing the following portfolio:
        {pretty_portfolio_data}

        Based on the data provided, give a detailed analysis of the portfolio's performance.
        PROVIDE THE ANALYSIS AND NOTHING ELSE!!
        """
        print(prompt)
        print("\nGenerating analysis using Ollama...\n")
        llm_analysis: str = ollama.generate(
            model='llama3.2',
            prompt=prompt,
        )
        print(llm_analysis['response'])

def convert_portfolio_data_to_string(portfolio_data: list[StockData]) -> str:
    return json.dumps([data.model_dump() for data in portfolio_data], indent=4)


if __name__ == "__main__":
    stock_data = [
        StockData(ticker='AAPL', buy_price=150.0, today_price=155.0, quantity=10),
        StockData(ticker='GOOGL', buy_price=2500.0, today_price=2550.0, quantity=5),
        StockData(ticker='AMZN', buy_price=3500.0, today_price=3600.0, quantity=3),
    ]
    LLM.get_portfolio_analysis(stock_data)
