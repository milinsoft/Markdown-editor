def unknown_command():
    print("Unknown formatting type or command")


def print_help():
    print("""Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done""")


def header():
    global text
    level = int(input("Level: "))
    if level not in range(1, 7):
        print("The level should be within the range of 1 to 6.")
        return header()
    txt = input("Text: ")
    text += f"{'#'*level} {txt}\n"
    print(text)


def plain():
    global text
    txt = input("Text: ")
    text += txt
    print(text)


def new_line():
    global text
    text += "\n"
    print(text)


def link():
    global text
    label = input("Label: ")
    url = input("URL: ")
    text += f"[{label}]({url})"
    print(text)


def bold():
    global text
    txt = input("Text: ")
    text += f"**{txt}**"
    print(text)


def italic():
    global text
    txt = input("Text: ")
    text += f"*{txt}*"
    print(text)


def inline_code():
    global text
    txt = input("Text: ")
    text += f"`{txt}`"
    print(text)


def ordered_list():
    global text
    rows_num = int(input("Number of rows: "))
    if rows_num <= 0:
        print("The number of rows should be greater than zero")
        return ordered_list()
    else:
        txt = [str(i) + ". " + input(f"Row #{i}: ") for i in range(1, rows_num + 1)]
        text += "\n".join(txt) + "\n"
        print(text)


def unordered_list():
    global text
    rows_num = int(input("Number of rows: "))
    if rows_num <= 0:
        print("The number of rows should be greater than zero")
        return unordered_list()
    else:
        txt = ["* " + input(f"Row #{i}: ") for i in range(1, rows_num + 1)]
        text += "\n".join(txt) + "\n"
        print(text)


def strike():
    global text
    # strikethrough font
    txt = input("Text: ")
    text += "~~", txt, "~~"
    print(text)


def save_to_file():
    with open("output.md", "w") as f1:
        f1.write(text)


text = ""
commands_list = {"plain", "bold", "italic", "header", "link", "inline-code", "new-line", "!help", "!done", "ordered-list", "unordered-list", "strike", "strikethrough"}


while True:
    formatter = input("Choose a formatter:")
    if formatter not in commands_list:
        unknown_command()
    elif formatter == "!help":
        print_help()
    elif formatter == "!done":
        save_to_file()
        break
    else:
        if formatter == "plain":
            plain()
        elif formatter == "bold":
            bold()
        elif formatter == "italic":
            italic()
        elif formatter == "header":
            header()
        elif formatter == "link":
            link()
        elif formatter == "inline-code":
            inline_code()
        elif formatter == "new-line":
            new_line()
        elif formatter == "ordered-list":
            ordered_list()
        elif formatter == "unordered-list":
            unordered_list()
        elif formatter in {"strike", "strikethrough"}:
            strike()
