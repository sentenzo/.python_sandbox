from table_drawer import TableDrawer
from table_drawer_md import MarkdownTableDrawer
from table_drawer_htmp import HtmlTableDrawer
from typing import List

class TableBuilder:
    def __init__(self) -> None:
        # self.drawer: TableDrawer = MarkdownTableDrawer()
        self.drawer: TableDrawer = HtmlTableDrawer()

        self.header: List[any] = None
        self.body: List[List[any]] = []
        self.coll_count: int = 0

    def set_header(self, header: List[any]) -> None:
        self.coll_count = max(self.coll_count, len(header))
        self.header = header

    def add_row(self, row: List[any]) -> None:
        self.coll_count = max(self.coll_count, len(row))
        self.body.append(row)

    def __str__(self) -> str:
        def align_row(row):
            diff = self.coll_count - len(row)
            row.extend([""] * diff)
            return row

        align_row(self.header)
        list(map(align_row, self.body))

        str_h = self.drawer.generateHeader
        str_r = self.drawer.generateRow
        tmp = [str_h(self.header)]
        n = len(self.body)
        for i, row in enumerate(self.body):
            tmp.append(str_r(row, i == n - 1))
        return "\n".join(tmp)

