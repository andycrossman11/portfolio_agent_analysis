import os
import json
import requests

class LLM():
    HOST = os.getenv("OLLAMA_HOST", "host.docker.internal")
    API_URL = f"http://{HOST}:11434"
    print(API_URL)

    @staticmethod
    def get_portfolio_analysis(portfolio_data: str) -> str:
        return LLM._get_analysis_from_llm(portfolio_data)
    
    @staticmethod
    def _get_analysis_from_llm(portfolio_data: str) -> str:
        llm_to_use = os.environ.get('LLM', None)
        if llm_to_use is None:
            return f"ANALYSIS: \n{portfolio_data}"
        elif llm_to_use == 'LLAMA3.2':
            return LLM._get_ollama_analysis(portfolio_data)
        
    @staticmethod
    def _get_ollama_analysis(portfolio_data: str) -> str:
        prompt: str = f"""
        You are a financial advisor and you have been given the task of analyzing the following portfolio:
        {portfolio_data}

        Based on the data provided, give a detailed analysis of the portfolio's performance.
        PROVIDE THE ANALYSIS AND NOTHING ELSE!!
        """
        print("\nGenerating analysis using Ollama...\n")

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'model': 'llama3.2',
            'prompt': prompt,
            'stream': False
        }

        response = requests.post(f"{LLM.API_URL}/api/generate", headers=headers, json=data)
        print(response)
        if response.status_code == 200:
            llm_analysis = response.json()
            return llm_analysis.get("response", "No response in the API output")
        else:
            return f"Error: {response.status_code}, {response.text}"
