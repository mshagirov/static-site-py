from pathlib import Path
from shutil import rmtree, copy
from os import get_terminal_size

root_dir = Path('.')
static_dir = root_dir / 'static'
public_dir = root_dir / 'public'

def get_terminal_width():
    try:
        width = get_terminal_size().columns // 2
    except OSError:
        width = 60
    return width

def clear_public_dir(logging=False):
    text_width = get_terminal_width()
    if logging:
        print(f'{"===[ Clearing : " + str(public_dir) + "/ ]":=<{text_width}}')
    
    if list(public_dir.iterdir()):
        if logging: print(f' deleting:')
    else:
        if logging: print(f' nothing to clear : "{str(public_dir)}/" is empty')

    for p in public_dir.iterdir():
        if p.is_dir():
            if logging: print(f'\u274c (directory) {str(p)}/')
            rmtree(p)
        else:
            if logging: print(f'\u274c {str(p)}')
            p.unlink()
    if logging:
        print(f'{"---[ Finished clearing : " + str(public_dir) + "/ ]":-<{text_width}}\n')

def copy_from_path_to_path(source, destination, logging=False):
    if not source.is_dir():
        if logging:
            print(source, '-->', destination / source.name)
        copy(source, destination / source.name)
        return

    if source != static_dir:
        destination = destination / source.name
        destination.mkdir()
    if logging:
        print(f'{str(source)}/ --> {str(destination)}/')

    for p in source.iterdir():
        copy_from_path_to_path(p, destination, logging)

def cp_static_to_public(logging=False):
    clear_public_dir(logging)  

    text_width = get_terminal_width()
    if logging:
        print(f'{"===[ Copying : " + str(static_dir) + "/ --> " + str(public_dir) + "/ ]":=<{text_width}}')

    if list(static_dir.iterdir()):
        if logging:
            print(f' copying:')

        copy_from_path_to_path(static_dir, public_dir, logging=logging)
    else:
        if logging: print(f' nothing to copy: "{str(static_dir)}/" is empty')
    
    if logging:
        print(f'{"---[ Finished copying : " + str(static_dir) + "/ --> " + str(public_dir) + "/ ]":-<{text_width}}\n')


