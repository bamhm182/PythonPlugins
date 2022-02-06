
import inspect
import types

from .plugins import loaded_functions
from ._state import State


class PluginMount(type):
    def __new__(cls, name, bases, attrs):
        for module in loaded_functions:
            name = module.__name__.replace(module.__package__, '').strip('.')
            plugin = types.ModuleType(name)
            for function_name, function in  inspect.getmembers(module, predicate=inspect.isfunction):
                setattr(plugin, function_name, function)
            attrs[name] = plugin
        return type.__new__(cls, name, bases, attrs)


class Handler(object, metaclass=PluginMount):
    def __init__(self):
        self.state = State()
