from typing import List
from table_drawer import TableDrawer

class HtmlTableDrawer(TableDrawer):
    @staticmethod
    def obj_to_str(obj):
        obj = str(obj)
        obj = obj.replace("&", "&amp;")
        obj = obj.replace("<", "&lt;")
        obj = obj.replace(">", "&gt;")
        return obj

    @staticmethod
    def list_map_str(lst):
        return list(map(HtmlTableDrawer.obj_to_str, lst))

    def generateHeader(self, header: List[any]) -> str:
        header = HtmlTableDrawer.list_map_str(header)
        line_0 = "<table>"
        line_1 = ("<tr>\n\t<th>" 
				  + "</th>\n\t<th>".join(header) 
				  + "</th>\n</tr>")
        return "\n".join([line_0, line_1])

    def generateRow(self, row: List[any], last: bool = False) -> str:
        row = HtmlTableDrawer.list_map_str(row)
        line = ("<tr>\n\t<td>" 
				+ "</td>\n\t<td>".join(row) 
				+ "</td>\n</tr>")
        if last:
            line += "\n</table>"
        return line
	
# <table>
# <tr>
#         <th>Action</th>
#         <th>Hotkey</th>
# </tr>
# <tr>
#         <td>Navigate forward</td>
#         <td>&lt;kbd&gt;Ctrl&lt;/kbd&gt; 
#             + &lt;kbd&gt;Alt&lt;/kbd&gt; 
#             + &lt;kbd&gt;→&lt;/kbd&gt;</td>
# </tr>
# <tr>
#         <td>Navigate back</td>
#         <td>Ctrl + Alt + ←</td>
# </tr>
# <tr>
#         <td>Create new note + switch</td>
#         <td>Ctrl + n</td>
# </tr>
# </table>