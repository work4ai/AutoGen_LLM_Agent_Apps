from autogen import AssistantAgent, UserProxyAgent

GROQ_API_KEY = "GROQ_API_KEY" #USE YOUR API KEY

llm_config = {
    "model": "llama3-70b-8192",  # Adjust to the desired Groq model
    "api_key": GROQ_API_KEY,
    "base_url": "https://api.groq.com/openai/v1",  # Ensure correct API endpoint
}

assistant = AssistantAgent("assistant", llm_config)
user_proxy = UserProxyAgent(
    "user_proxy",
    llm_config=llm_config,
    code_execution_config={
        "workd_dir": "code_execution",
        "use_docker": False,
    },
    human_input_mode="NEVER",
)

# start the agents
user_proxy.initiate_chat(
    assistant,
    message="What is the capital of France?",
)
