from api_original import ApiOriginal
from obj_adapter import ObjAdapter
from cls_adapter import ClsAdapter

def do_something_with_messages(api: ApiOriginal) -> None:
    messages = api.getMessages_GET()
    print(*messages, sep="\n")


def main():
    api: ApiOriginal = ApiOriginal()
    do_something_with_messages(api)

    api: ApiOriginal = ObjAdapter()
    do_something_with_messages(api)

    api: ApiOriginal = ClsAdapter()
    do_something_with_messages(api)


if __name__ == "__main__":
    main()