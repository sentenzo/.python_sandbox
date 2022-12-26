from search_builder import SearchQueryBuilder_Sys1, SearchQueryBuilder_Sys2
from director import Director

def main():
    builder = SearchQueryBuilder_Sys1()

    builder.reset()
    builder.searchInContent("to be or not to be")
    builder.include_tags(["poetry", "lyrics"])
    builder.exclude_tags(["digest"])
    print(builder.getResult())

    Director().makeSimpleSearch(builder, "search me")
    print(builder.getResult())

    builder = SearchQueryBuilder_Sys2()
    Director().makeSearchWithTags(
        builder, "to be or not to be", ["poetry", "lyrics"])
    print(builder.getResult())

if __name__ == "__main__":
    main()