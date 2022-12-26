from typing import List
from search_builder import SearchBuilder

class Director:
    def makeSimpleSearch(self, builder: SearchBuilder
						 , query: str) -> None:
        builder.reset()
        builder.searchInTitle(query)
        builder.searchInContent(query)
        builder.strict(False)

    def makeSearchWithTags(self, builder: SearchBuilder
						   , query: str, tags: List[str]) -> None:
        builder.reset()
        builder.searchInTitle(query)
        builder.searchInContent(query)
        builder.include_tags(tags)
        builder.strict(False)