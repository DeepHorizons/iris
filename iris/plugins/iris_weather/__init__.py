"""
"""
from iris.plugins import Plugin


class IrisWeather(Plugin):

    def weather(*args, **kwargs):
        """ Functions must accept any number of args and kwargs
        """
        return {'text': "The weather is partly cloudy with a chance of rain"}

    def weather2(*args, **kwargs):
        if 'today' in kwargs['text']:
            return {'text': "The weather today is sunny"}
        else:
            return {'text': "The weather tomorrow is AM rain"}

    grammar = {
        "Whats the weather": weather,  # Static methods store the function under __func__
        "whats the weather [today|tomororw]": weather2,
    }
