from __future__ import annotations
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Prototype: pass