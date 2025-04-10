# from typing import Text
from pathlib import Path
import sys

from cp_static_to_public import cp_static_to_public
from generate_pages_recursive import generate_pages_recursive


def main(basepath='/'):
    cp_static_to_public(static_dir=Path("./static"),public_dir=Path("./docs"), logging=True)

    source_md_path   = Path("./content")
    template_path    = Path("./template.html")
    # use ./public for local testing
    target_html_path = Path("./docs")
    
    generate_pages_recursive(source_md_path, template_path, target_html_path, basepath)

if __name__ == '__main__':
    if len(sys.argv)>1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    # excute when called from CLI
    main(basepath)
