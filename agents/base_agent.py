from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    """
    Abstract base class for all AI agents.
    Every agent in the platform must inherit from this class.
    """

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

    @abstractmethod
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        pass

    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def reset(self) -> None:
        self.status = "idle"
