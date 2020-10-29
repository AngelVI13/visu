from abc import ABC, abstractmethod


class BaseView(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def register_inputs(self, *args, **kwargs):
        pass