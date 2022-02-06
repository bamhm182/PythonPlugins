
import inspect

from .plugins import loaded_functions
from ._state import State



class PluginMount(type):
    def __new__(cls, name, bases, attrs):
        for module in loaded_functions:
            funcs = dict()
            for function_name, function in  inspect.getmembers(module, predicate=inspect.isfunction):
                funcs[function_name] = function
            plugin = module.__name__.replace(module.__package__, '').strip('.')
            attrs[plugin] = type.__new__(cls, 'plugin', (object,), funcs)
        return type.__new__(cls, name, bases, attrs)


class Handler(object, metaclass=PluginMount):
    def __init__(self):
        self.state = State()
