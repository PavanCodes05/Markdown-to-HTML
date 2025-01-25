def template(file_path):
    with open(file_path, "r") as file:
        contents = file.readlines()
    return contents

def generate_html(contents):
    tags = []

    for content in contents:
        # Heading
        if content[0] == "#":
            count = content.count("#")
            value = content[count: ]

            tag = f"<h{count}>{value.strip()}</h{count}>"        
            tags.append(tag)

        # Bold
        elif content[0] == "*" and content[1] == "*":
            value = content.strip("**")
            
            tag = f"<b>{value}</b>"
            tags.append(tag)

        # Italic
        elif content[0] == "_":
            value = content.strip("_")

            tag = f"<em>{value}</em>"
            tags.append(tag)

    return tags

def create_html(template_contents, html_contents, pos):
    tags = ""
    for content in html_contents:
        tags += content
    
    template_contents[pos] = tags

    file_content = template_contents

    return file_content

def generate_output(path, file_contents):
    with open(path, "w") as file:
        for content in file_contents:
            file.write(content)
    
    print("Output Generated!")
    