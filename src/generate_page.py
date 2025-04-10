from pathlib import Path

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path:Path, template_path:Path, dest_path:Path, basepath="/"):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path) as f:
        md = f.read()

    with open(template_path) as f:
        template_html = f.read()

    content_html  = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    final_html = template_html.replace(
        "{{ Title }}", title
    ).replace(
        "{{ Content }}", content_html
    ).replace(
        'href="/', f'href="{basepath}'
    ).replace(
        'src="/', f'src="{basepath}'
    )

    if not dest_path.name.endswith(".html"):
        dest_path = dest_path / (from_path.name[:-3] + ".html")

    if not dest_path.parent.exists():
        dest_path.parent.mkdir(parents=True)

    with open(dest_path, "w") as f:
        f.write(final_html)

