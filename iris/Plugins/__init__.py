"""

"""

from abc import ABCMeta, abstractmethod, abstractproperty


class Plugin(metaclass=ABCMeta):

    @abstractproperty
    def grammars(self) -> dict:
        pass
