from langchain_core.messages import BaseMessage


class Memory:
    def __init__(self):
        self._messages: list[BaseMessage] = []

    def add(self, message: BaseMessage) -> None:
        self._messages.append(message)

    def get(self) -> list[BaseMessage]:
        return self._messages

    def clear(self) -> None:
        self._messages.clear()