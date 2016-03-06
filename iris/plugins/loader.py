import importlib
import os
from iris.plugins import *


def _load_plugins():
    """
    Load all plugins
    :return:
    """
    # import all plugins
    # use an envvar to locate the folder?
    file_path = os.path.dirname(__file__)
    import iris.plugins
    libs = [d for d in os.listdir(file_path) if os.path.isdir(file_path + '/' + d)]
    #print(libs)
    [importlib.import_module('iris.plugins.' + i) for i in libs]
    pass


def _get_all_plugins():
    return Plugin.__subclasses__()


def _get_plugin_grammar(p):
    return p.grammar


def get_all_grammars():
    _load_plugins()  # Reload all plugins to reflect changes

    a = {}
    for plug in _get_all_plugins():
        plug = plug()  # Instantiate the class
        a.update(_get_plugin_grammar(plug))
    return a
