"""
"""
from iris.plugins import Plugin


class IrisWeather(Plugin):

    def weather(*args, **kwargs):
        """ Functions must accept any number of args and kwargs
        """
        return {'text': "The weather is partly cloudy with a chance of rain"}

    grammar = {
        "Whats the weather": weather,  # Static methods store the function under __func__
    }
