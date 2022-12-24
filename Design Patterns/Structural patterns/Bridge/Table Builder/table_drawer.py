from abc import ABC, abstractmethod
from typing import List

class TableDrawer(ABC):
    @abstractmethod
    def generateHeader(self, header: List[any]) -> str: pass

    @abstractmethod
    def generateRow(self, row: List[any]
					, last: bool = False) -> str: pass