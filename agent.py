from config import Config
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import calculate_math_expression
from langchain_core.messages import ToolMessage, HumanMessage
from memory import Memory

model = ChatGoogleGenerativeAI(
    model = Config.MODEL_NAME,
    api_key = Config.GOOGLE_API_KEY
)

model = model.bind_tools([calculate_math_expression])

memory = Memory()

def chat(user_input: str):

    human_message = HumanMessage(content=user_input)
    memory.add(human_message)

    response = model.invoke(memory.get())
    memory.add(response)

    if response.tool_calls:

        tool_call = response.tool_calls[0]

        expression = tool_call["args"].get("expression")
        
        result = calculate_math_expression.invoke(
        {"expression": expression}
        )

        tool_message = ToolMessage(
            content=str(result),
            tool_call_id=tool_call["id"]
        )

        memory.add(tool_message)

        final_response = model.invoke(memory.get())
        memory.add(final_response)

        content = final_response.content

        if isinstance(content, list):

            return "".join(
                block["text"]
                for block in content
                if block.get("type") == "text"
            )

    return content
