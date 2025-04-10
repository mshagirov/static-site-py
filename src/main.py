# from typing import Text
from pathlib import Path

from cp_static_to_public import cp_static_to_public
from genarate_all_pages import generate_all_pages

def main():
    cp_static_to_public(logging=True)

    source_md_path   = Path("./content")
    template_path    = Path("./template.html")
    target_html_path = Path("./public")
    
    generate_all_pages(source_md_path, target_html_path, template_path)

if __name__ == '__main__':
    # excute when called from CLI
    main()
