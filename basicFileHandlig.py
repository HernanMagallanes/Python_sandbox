
from pathlib import Path
import os

# window \ backslashes
# macOS and Linux / forward slash

subfolder = Path('there', 'general')
homefolder = Path('hello')
print(homefolder / subfolder)

# Current Working directory
# print(Path.cwd())
# change dir with chdir()

# Home directory
# print(Path.home())

# New dir
# os.mkdir(path)
# Path(r'').mkdir()

# Parts of a file path
p = Path.cwd()
print(p)
print(f'parent: {p.parent}')
print(f'name: {p.name}')
print(f'stem: {p.stem}')
print(f'suffix: {p.suffix}')
print(f'drive: {p.drive}')
print('')

print(f'dirname: {os.path.dirname(p)}')
print(f'basename: {os.path.basename(p)}')
print('')

# path validity
print(p.exists())
print(p.is_dir())
print(p.is_file())
print('')

# File reading / writing process
p = Path('spam.txt')
p.write_text('Hello world !')
print(p.read_text())

# steps: open() , read() , close()
# open() modes: write 'w' , append 'a'
