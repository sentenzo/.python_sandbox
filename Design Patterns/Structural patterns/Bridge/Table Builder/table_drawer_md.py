from typing import List
from table_drawer import TableDrawer

class MarkdownTableDrawer(TableDrawer):
    @staticmethod
    def obj_to_str(obj):
        obj = str(obj)
        return obj.replace("|", "\\|")

    @staticmethod
    def list_map_str(lst):
        return list(map(MarkdownTableDrawer.obj_to_str, lst))

    def generateHeader(self, header: List[any]) -> str:
        header = MarkdownTableDrawer.list_map_str(header)
        line_0 = " | ".join(header)
        line_1 = "|-"*len(header) + "|"
        return "\n".join([line_0, line_1])

    def generateRow(self, row: List[any], last: bool = False) -> str:
        row = MarkdownTableDrawer.list_map_str(row)
        return " | ".join(row)
