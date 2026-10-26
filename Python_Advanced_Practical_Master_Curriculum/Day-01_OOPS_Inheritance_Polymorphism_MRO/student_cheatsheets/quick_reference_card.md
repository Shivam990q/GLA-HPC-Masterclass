# Day 1 Cheatsheet: Python OOPS Quick Reference

```python
# Encapsulation & Properties
class Model:
    def __init__(self, val):
        self._val = val
    @property
    def val(self): return self._val
    @val.setter
    def val(self, v): self._val = v

# Abstract Base Class
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def run(self): pass

# Inspection
isinstance(obj, ClassName)
issubclass(Sub, Super)
Class.mro() # Shows Method Resolution Order
```
