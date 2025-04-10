# from typing import Text
from pathlib import Path

from cp_static_to_public import cp_static_to_public
from generate_pages_recursive import generate_pages_recursive

def main():
    cp_static_to_public(logging=True)

    source_md_path   = Path("./content")
    template_path    = Path("./template.html")
    target_html_path = Path("./public")
    
    generate_pages_recursive(source_md_path, template_path, target_html_path)

if __name__ == '__main__':
    # excute when called from CLI
    main()
