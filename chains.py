from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Act as a critique for twitter post
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're a viral Twitter influencer grading a tweet. Generate critique and recommendation for the user's tweet."
            "Always provide detailed recommendations including requests for length, virality, style, etc.."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Twitter techie influencer assistant tasked with writing excellent Twitter posts."
            "Generate the best Twitter posts possible for the user's request."
            "If the user provides critique, respond with a revised version of your previous attempts"
        ),

        MessagesPlaceholder(variable_name="messages")
       
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini")
generate_chain= generation_prompt | llm
reflection_chain= reflection_prompt | llm