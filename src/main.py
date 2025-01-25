import os

from parser import read_markdown, find_body_pos
from generator import template, generate_html, create_html, generate_output

markdown_contents = read_markdown("examples\sample.md")

modified_contents = []

for line in markdown_contents:
    if line == "\n":
        continue
    
    modified_contents.append(line.strip().rstrip())

html_contents = generate_html(modified_contents)

# Create a directory for saving html files
directory = "src/public"
file_name = "sample.html"

os.makedirs(directory, exist_ok=True)

file_path = os.path.join(directory, file_name)

# Create a HTML file
template_contents = template("src\/templates\/template.html")
body_pos = find_body_pos(template_contents)

file_contents = create_html(template_contents, html_contents, body_pos)

generate_output(file_path, file_contents)