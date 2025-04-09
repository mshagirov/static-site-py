from pathlib import Path
from shutil import rmtree, copy
from os import get_terminal_size
from types import ClassMethodDescriptorType

root_dir = Path('.')
static_dir = root_dir / 'static'
public_dir = root_dir / 'public'


def clear_public_dir():
    text_width = get_terminal_size().columns // 2
    print(f'{"=== Clearing : [ " + str(public_dir) + "/ ] ":=<{text_width}}')
    if list(public_dir.iterdir()):
        print(f' deleting:')
    else:
        print(f' nothing to clear : "{str(public_dir)}/" is empty')

    for p in public_dir.iterdir():
        if p.is_dir():
            print(f'\u274c (directory) {str(p)}/')
            rmtree(p)
        else:
            print(f'\u274c {str(p)}')
            p.unlink()
    print(f'{"--- Finished clearing : [ " + str(public_dir) + "/ ] ":-<{text_width}}\n')

def copy_from_path_to_path(source, destination):
    if not source.is_dir():
        print(source, '-->', destination / source.name)
        copy(source, destination / source.name)
        return

    if source != static_dir:
        destination = destination / source.name
        destination.mkdir()

    print(f'{str(source)}/ --> {str(destination)}/')

    for p in source.iterdir():
        copy_from_path_to_path(p, destination)

def cp_static_to_public():
    clear_public_dir()  

    text_width = get_terminal_size().columns // 2
    print(f'{"=== Copying : [ " + str(static_dir) + "/ ] -->  [ " + str(public_dir) + "/ ] ":=<{text_width}}')

    if list(static_dir.iterdir()):
        print(f' copying:')
        copy_from_path_to_path(static_dir, public_dir)
    else:
        print(f' nothing to copy: "{str(static_dir)}/" is empty')

    print(f'{"--- Finished copying : [ " + str(static_dir) + "/ ] -->  [ " + str(public_dir) + "/ ] ":-<{text_width}}\n')


