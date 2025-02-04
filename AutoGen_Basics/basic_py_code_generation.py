from autogen import AssistantAgent, UserProxyAgent

GROQ_API_KEY = "GROQ_API_KEY" #USE YOUR API-KEY

llm_config = {
    "model": "llama3-70b-8192",  # Adjust to the desired Groq model
    "api_key": GROQ_API_KEY,
    "base_url": "https://api.groq.com/openai/v1",  # Ensure correct API endpoint
}

assistant = AssistantAgent(
    name="Assistant",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # make it True if you want to use docker
    },
)

user_proxy.initiate_chat(
    assistant, message="Plot a chart of META and TESLA stock price change."
)


######################OUTPUT GENERATED PYTHON CODE#################################################
'''
# filename: stock_price_chart.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch META and TESLA stock price data
meta_data = yf.download('META', start='2020-01-01', end='2022-12-31')
tesla_data = yf.download('TSLA', start='2020-01-01', end='2022-12-31')

# Plot the stock price changes
plt.plot(meta_data.index, meta_data['Close'], label='META')
plt.plot(tesla_data.index, tesla_data['Close'], label='TSLA')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('META and TESLA Stock Price Change')
plt.legend()
plt.show()
'''

