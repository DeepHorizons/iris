"""
"""
from iris.plugins import Plugin


class IrisWeather(Plugin):
    grammar = {
        "Whats the weather": str,  # Static methods store the function under __func__
    }