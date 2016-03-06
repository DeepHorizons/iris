"""

"""

from abc import ABCMeta, abstractmethod, abstractproperty


class IrisPlugin(metaclass=ABCMeta):
    """
    A dummy class to specify that the sub classes are plugins

    The plugin must implement a list of dictionaries that have the structure
    {grammar: function}
    This can be implemented as a singleton, instance, or property

    grammar is a string representing what text it is looking for
    function is the function to call if the the grammar is matched

    function must return a dictionary populated with whatever data is necessary
    """

    @property
    def grammar(self):
        """
        Dont use the ABC on this as the plugin can implement the grammar in different ways
        see sample plugins
        """
        raise NotImplementedError("The grammar was not implemented")
