import os
import json
import ollama


class LLM():
    host = os.getenv("OLLAMA_HOST", "host.docker.internal")

    ollama.api_base = f"http://{host}:11434"

    @staticmethod
    def get_portfolio_analysis(portfolio_data: str) -> str:
        return LLM._get_analysis_from_llm(portfolio_data)
    
    @staticmethod
    def _get_analysis_from_llm(portfolio_data: str) -> str:
        llm_to_use = os.environ.get('LLM', None)
        print(llm_to_use)
        if llm_to_use is None:
            return f"ANALYSIS: \n{portfolio_data}"
        elif llm_to_use == 'LLAMA3.2':
            print("here")
            return LLM._get_ollama_analysis(portfolio_data)
        
    @staticmethod
    def _get_ollama_analysis(portfolio_data: str) -> str:
        prompt: str = f"""
        You are a financial advisor and you have been given the task of analyzing the following portfolio:
        {portfolio_data}

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
