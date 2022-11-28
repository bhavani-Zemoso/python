from contextlib import suppress, redirect_stdout

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

path = 'text.txt'

with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)