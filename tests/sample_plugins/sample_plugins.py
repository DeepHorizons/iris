"""
Sample plugins
"""

from iris.plugins import Plugin


def weather(*args, **kwargs):
    """ Functions must accept any number of args and kwargs
    """
    return {'text': "The weather is partly cloudy with a chance of rain"}


def temp(*args, **kwargs):
    """ Functions must accept any number of args and kwargs
    """
    return {'text': "The temperature is 79 degrees"}


class Sample1Plugin(Plugin):
    """
    Implement the grammar on the class
    """
    grammar = {
        "Whats the weather": weather,  # Static methods store the function under __func__
    }


class Sample2Plugin(Plugin):
    """
    Init the grammar on the init of the class
    """
    def __init__(self):
        # Some init code
        self._grammar = {
            "Whats the temperature": temp,  # Static methods store the function under __func__
        }
        return

    @property
    def grammar(self):
        return self._grammar


class Sample3Plugin(Plugin):
    """
    Define a property that returns the grammar
    """
    @property
    def grammar(self):
        return {
            "Whats the weather": str,  # Static methods store the function under __func__
        }

if __name__ == '__main__':
    [i() for i in Plugin.__subclasses__()]
