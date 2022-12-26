from abc import ABC, abstractmethod
from typing import List
from search_query import SearchQuery_Sys1, SearchQuery_Sys2

class SearchBuilder(ABC):
    @abstractmethod
    def reset(self) -> None: pass
    @abstractmethod
    def strict(self) -> None: pass
    @abstractmethod
    def include_tags(self, tags: List) -> None: pass
    @abstractmethod
    def exclude_tags(self, tags: List) -> None: pass
    @abstractmethod
    def searchInTitle(self, text) -> None: pass
    @abstractmethod
    def searchInContent(self, text) -> None: pass

class SearchQueryBuilder_Sys1(SearchBuilder):
    def __init__(self) -> None:
        self.reset()
    def reset(self) -> None:
        query = SearchQuery_Sys1()
        query.case_sensitive = False
        query.reg_ex = False
        query.strict = False
        query.included_tags = []
        query.excluded_tags = []
        self.query = query

    def strict(self, val: bool = True) -> None:
        self.query.strict = val
        self.query.case_sensitive = val

    def include_tags(self, tags: List) -> None:
        self.query.included_tags += tags

    def exclude_tags(self, tags: List) -> None:
        self.query.excluded_tags += tags

    def searchInTitle(self, text) -> None:
        self.query.search_in_title = text

    def searchInContent(self, text) -> None:
        self.query.search_in_content = text

    def getResult(self) -> SearchQuery_Sys1:
        return self.query


class SearchQueryBuilder_Sys2(SearchBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        query = SearchQuery_Sys2()
        query.case_sensitive = False
        query.search_in_content = []
        self.query = query

    def strict(self, val: bool = True) -> None:
        self.query.case_sensitive = val

    def include_tags(self, tags: List) -> None:
        for tag in tags:
            self.query.search_in_content.append(
                f"<tag>{tag}</tag>")

    def exclude_tags(self, tags: List) -> None:
        for tag in tags:
            self.query.search_in_content.append(
                f"<exclude><tag>{tag}</tag></exclude>")

    def searchInTitle(self, text) -> None:
        self.query.search_in_content.append(
            f"<title>{text}</title>")

    def searchInContent(self, text) -> None:
        self.query.search_in_content.append(
            f"<context>{text}</context>")

    def getResult(self) -> SearchQuery_Sys2:
        self.query.search_in_content = "".join(self.query.search_in_content)
        return self.query