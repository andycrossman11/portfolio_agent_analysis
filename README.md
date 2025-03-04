# portfolio_agent_analysis
A full stack web app to automatically generate daily portfolio performance analysis with Llama3.2


## To get full Application Functionality, have the following:
- alpha_vantage API key set at ./api/src/portfolio_management/.env
- Ollama install on local machine
- llama3.2 pulled onto your local machine with Ollama
- Set LLM=LLAMA3.2 at ./api/src/portfolio_management/.env

## How to Run
- Ensure you have docker and docker-compose installed
- Simply run docker-compose up --build
- UI will be running on **http://localhost:3000**
- API docs availabel at **http://localhost:8000/docs**
- Can also utilize Docker Desktop to view the 5 container logs