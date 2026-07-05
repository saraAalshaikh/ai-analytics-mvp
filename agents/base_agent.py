#base Agent
from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.status = "idle"

    def get_info(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status,
        }

    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        return isinstance(input_data, dict)

    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def reset(self) -> None:
        self.status = "idle"
