def generate_html(contents):
    tags = []

    for content in contents:
        # Heading
        if content[0] == "#":
            count = content.count("#")
            value = content[count: ]

            tag = f"<h{count}>{value.strip()}<h{count}>"        
            tags.append(tag)

    return tags