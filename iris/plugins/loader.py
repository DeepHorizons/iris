import importlib
import os
import sys
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

    # Reload already loaded plugins
    plugins = Plugin.__subclasses__()
    reloaded_plugins = [importlib.reload(sys.modules[i.__module__]) for i in plugins]

    # Import any new ones if they were not reloaded
    libs = ['iris.plugins.' + d for d in os.listdir(file_path) if os.path.isdir(file_path + '/' + d)]
    imported_plugins = [importlib.import_module(i) for i in libs if i not in [d.__name__ for d in reloaded_plugins]]
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
