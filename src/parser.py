def read_markdown(file):
    try:
        with open(file) as md:
            content = md.readlines()
        return content
    except FileNotFoundError:
        print("Sorry the markdown file is not found!")

def find_body_pos(template_contents):
    for i in range(len(template_contents)):
        if template_contents[i].strip().rstrip() == "<!-- Insert here -->":
            return i