import importlib, pkgutil


loaded_functions = list()
for importer, modname, ispkg in pkgutil.iter_modules(__path__):
    loaded_functions.append(importlib.import_module('{}.{}'.format(__package__, modname)))
