from typing import List

class SearchQuery_Sys1:
    def __init__(self) -> None:
        self.case_sensitive: bool = None
        self.reg_ex: bool = None
        self.search_in_title: str = None
        self.search_in_content: str = None
        self.strict: bool = None
        self.included_tags: List[str] = None
        self.excluded_tags: List[str] = None

    def getSearchQueryString(self) -> str:
        return (f"╔══════════════════╼═╼═╼─ ─ ─ ╴ ╴ ╴\n" +
                f"║ case_sensitive: {('NO', 'YES')[self.case_sensitive]}\n" +
                f"║ reg_ex: {('NO', 'YES')[self.reg_ex]}\n" +
                f"║ strict: {('NO', 'YES')[self.strict]}\n" +
                f"║ search_in_title: {self.search_in_title}\n" +
                f"║ search_in_content: {self.search_in_content}\n" +
                f"║ included_tags: {self.included_tags}\n" +
                f"║ excluded_tags: {self.excluded_tags}\n" +
                f"╚══════════════════╼═╼═╼─ ─ ─ ╴ ╴ ╴"
                )
    def __str__(self) -> str:
        return self.getSearchQueryString()

class SearchQuery_Sys2:
    def __init__(self) -> None:
        self.case_sensitive: bool = None
        self.search_in_content: str = None
    def getSearchQueryString(self) -> str:
        return (f"░███▛▞▞▞▞▞▞▞▞▞▗▝ ▗ ▝  ▗   ▝\n" +
                f"░█  case_sensitive: {('NO', 'YES')[self.case_sensitive]}\n" +
                f"░█  search_in_content: {self.search_in_content}\n" +
                f"░███▙▚▚▚▚▚▚▚▚▚▝▗ ▝ ▗  ▝   ▗"
                )
    def __str__(self) -> str:
        return self.getSearchQueryString()