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
    [importlib.import_module(i) for i in (d for d in os.listdir(os.curdir) if os.path.isdir(d))]
    pass


def _get_all_plugins():
    return IrisPlugin.__subclasses__()


def _get_plugin_grammar(p):
    return p.grammar


def get_all_grammars():
    _load_plugins()  # Reload all plugins to reflect changes

    a = {}
    for plug in _get_all_plugins():
        plug = plug()  # Instantiate the class
        a.update(_get_plugin_grammar(plug))
    return a
