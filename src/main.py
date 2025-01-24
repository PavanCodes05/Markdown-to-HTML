from parser import read_markdown
from generator import generate_html

markdown_contents = read_markdown("examples\sample.md")

modified_contents = []

for line in markdown_contents:
    if line == "\n":
        continue
    
    modified_contents.append(line.rstrip())

html_contents = generate_html(modified_contents)
print(html_contents)