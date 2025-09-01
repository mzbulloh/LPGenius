from langchain.chat_models import AzureChatOpenAI

OPENAI_API_KEY = "4QQWElITIFiMC9JMp9T6clC6jTRTpm7B9cLtF3vTzw0sOfmsi23FJQQJ99BEACYeBjFXJ3w3AAABACOGnPE1"
OPENAI_API_BASE = "https://lpgenius.openai.azure.com/"
OPENAI_API_VERSION = "2025-01-01-preview"

llm = AzureChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    openai_api_base=OPENAI_API_BASE,
    openai_api_version=OPENAI_API_VERSION,
    deployment_name="gpt-4o-mini"  
)

def lpgenius_chat(prompt):
    response = llm.invoke([
        {"role": "system", "content": "LPGenius, asisten LPG subsidi dalam Bahasa Indonesia."},
        {"role": "user", "content": prompt}
    ])
    return response.content