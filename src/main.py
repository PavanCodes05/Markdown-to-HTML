from parser import read_markdown

markdown_contents = read_markdown("examples\sample.md")

modified_contents = []

for line in markdown_contents:
    if line == "\n":
        continue
    
    modified_contents.append(line.rstrip())
