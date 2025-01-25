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