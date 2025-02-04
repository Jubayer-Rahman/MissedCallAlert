from abc import ABC, abstractmethod

class NotificationAbstract(ABC):
    @abstractmethod
    def send_notification(self, message: str, recipient: str) -> str:
        pass