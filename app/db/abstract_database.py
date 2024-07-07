from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass

    @abstractmethod
    def fetch_one(self):
        pass

    @abstractmethod
    def fetch_all(self):
        pass
