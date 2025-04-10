from pathlib import Path

from generate_page import generate_page


def generate_pages_recursive(source_md_path:Path, template_path:Path, target_html_path:Path, basepath="/"):
    from_md_to_html_paths = []
    
    def get_md_to_html_paths(source_path:Path):
        if source_path.is_file() and (source_path.suffix == '.md'):
            new_path = str(source_path).replace(str(source_md_path), str(target_html_path), 1)
            new_path = Path(new_path.replace(".md", ".html"))
            from_md_to_html_paths.append((source_path, new_path))
        if source_path.is_dir():
            for p in source_path.iterdir():
                get_md_to_html_paths(p)

    assert source_md_path.is_dir()
    assert target_html_path.is_dir()

    get_md_to_html_paths(source_md_path)
    
    for from_path, dest_path in from_md_to_html_paths:
        generate_page(from_path, template_path, dest_path, basepath)

