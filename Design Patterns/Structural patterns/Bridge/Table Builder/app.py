from table_builder import TableBuilder

def main() -> None:
    tb = TableBuilder()
    tb.set_header(["Action", "Hotkey"])
    tb.add_row(
        ["Navigate forward"
		 , "<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>→</kbd>"])
    tb.add_row(["Navigate back", "Ctrl + Alt + ←"])
    print(tb)
    tb.add_row(["Create new note + switch", "Ctrl + n"])
    print(tb)
    tb.set_header(["Action", "Hotkey 1", "Hotkey 2"])
    tb.add_row(["Open help", "<kbd>F1</kbd>",
               "<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>h</kbd>"])
    print(tb)

if __name__ == "__main__":
    main()