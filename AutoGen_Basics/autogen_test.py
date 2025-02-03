from autogen import ConversableAgent

# Initialize GROQ LLM
GROQ_API_KEY = "GROQ_API_KEY" #Provide your own GROQ API Key

# Initialize the Groq client
#client = groq.Client(api_key=GROQ_API_KEY)

llm_config = {
    "model": "llama3-70b-8192",  # Adjust to the desired Groq model
    "api_key": GROQ_API_KEY,
    "base_url": "https://api.groq.com/openai/v1",  # Ensure correct API endpoint
}

agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "Tell me a funny joke."}]
)

print(response)
