def read_markdown(file):
    try:
        with open(file) as md:
            content = md.readlines()
        return content
    except FileNotFoundError:
        print("Sorry the markdown file is not found!")
