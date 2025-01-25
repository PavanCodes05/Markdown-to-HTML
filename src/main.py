import os

from parser import read_markdown
from generator import template, generate_html

template_contents = template("src\/templates\/template.html")

markdown_contents = read_markdown("examples\sample.md")

modified_contents = []

for line in markdown_contents:
    if line == "\n":
        continue
    
    modified_contents.append(line.rstrip())

html_contents = generate_html(modified_contents)

# Create a HTML file
directory = "src/public"
file_name = "sample.html"

os.makedirs(directory, exist_ok=True)

file_path = os.path.join(directory, file_name)

print(file_path)
with open(file_path, 'w') as file:
    for content in template_contents:
        file.write(content)