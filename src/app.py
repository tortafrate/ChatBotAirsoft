from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

chat = ChatOllama(
    model_name="mistral:instruct",
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a comedian who tell joke about: ",
        ),
        ("human", "{topic}"),
    ]
)

chain = prompt | chat | StrOutputParser()

print(chain.invoke({"topic": "Bomboclaat"}))
