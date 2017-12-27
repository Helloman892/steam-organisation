#!/bin/python3
import sys
from collections import Counter


def remove_duplicates(val):
    output = []
    seen = set()
    for j in val:
        if j not in seen:
            output.append(j)
            seen.add(j)
    return output


def sort_keys(fname):
    lst = []
    full = fname.split('.')
    fname = full[0]
    ext = '.' + full[-1] if len(full) > 1 else ''
    try:
        with open(fname + ext) as f:
            seen = set()
            for idx, line in enumerate(f):
                if line and line != '\n' and line not in seen:
                    try:
                        if line.split('| ')[1][:3] == 'DLC':
                            lst.append((f'z{line.split("| ")[1]}', line))
                        else:
                            lst.append((line.split('| ')[1], line))
                        if not all(len(i) == 5 for i in line.split(' |')[0].split('-'))\
                                or len(line.split(' |')[0]) != 17:
                            if line.split('|')[1]:
                                print(f'Malformed key-name pair on line {idx + 1}: {line[:-1]}')
                            else:
                                print(f'Malformed key on line {idx + 1}: {line.split("| ")[1]}')
                    except IndexError:
                        print(f'Missing name on line {idx + 1}: {line[:-3]}')
                seen.add(line)

        sorted_lst = sorted(lst, key=lambda k: k[0])

        with open(f'{fname}_sorted{ext}', 'w') as f_s:
            for i in sorted_lst:
                f_s.write(f'{i[1]}')

        # Pulls together multiple keys for the same game
        rem = iter(remove_duplicates(sorted_lst))
        counter = Counter(i[0][1:] if i[0][:4] == 'zDLC'
                          else i[0] for i in remove_duplicates(sorted_lst))

        with open(f'{fname}_list{ext}', 'w') as f_l:
            for i in rem:
                name = i[0][1:] if i[0][:4] == 'zDLC' else i[0]
                if counter.get(name) == 1:
                    f_l.write(f'{name}')
                else:
                    f_l.write(f'{name[:-1]} * {counter.get(name)}\n')
                    for j in range(1, counter.get(name)):
                        next(rem)
            f_l.write(f'\nTotal keys: {len(sorted_lst)}\n')
    except FileNotFoundError:
        print(f'{fname} does not exist.')
    except IsADirectoryError:
        print(f'{fname} is a directory.')
    except PermissionError:
        print(f'You do not have rights to {fname}.')


def add_keys(fname, lst):
    # Joins args by spaces, then splits by commas. This allows for something similar to a CSV from a list.
    lst = [f"{i.split(' ')[0]} | {' '.join(i.split(' ')[1:])}\n" for i in ' '.join(lst).split(', ')]
    try:
        with open(fname, 'a+') as f:
            f.writelines(lst)
    except FileNotFoundError:
        print(f'{fname} does not exist.')
    except IsADirectoryError:
        print(f'{fname} is a directory.')
    except PermissionError:
        print(f'You do not have rights to {fname}.')


def pop_keys(fname, lst):
    lst = ' '.join(lst).split(', ')
    try:
        with open(fname, 'r') as f_l:
            lines = f_l.read().splitlines()
        with open(fname, 'w') as f:
            print('Analysis complete:')
            skip = [None] * len(lines)
            for key in lst:
                for idx, line in enumerate(lines):
                    if skip[idx]:
                        continue
                    tem = line.split(' | ')
                    try:
                        if tem[0] == key:
                            print(line)
                            lines.remove(line)
                            break  # Only deletes the first instance
                        elif tem[1] == key:
                            print(line)
                            lines.remove(line)
                            break  # Only deletes the first instance
                    except IndexError:
                        skip[idx] = True
            lines = [line + '\n' for line in lines]
            f.writelines(lines)
    except FileNotFoundError:
        print(f'{fname} does not exist.')
    except IsADirectoryError:
        print(f'{fname} is a directory.')
    except PermissionError:
        print(f'You do not have rights to {fname}.')


if __name__ == '__main__':
    try:
        cmd = sys.argv[1]
    except IndexError:
        cmd = None
    if cmd == 'add':
        try:
            add_keys(sys.argv[2], sys.argv[3:])
        except IndexError:
            print('Usage: sort_keys add [file] [keys]\n'
                  '\nwhere keys is a comma separated list of Steam keys'
                  '\nin the format `XXXXX-XXXXX-XXXXX name`.'
                  '\nPrepend `name` with \'DLC: \' if it is addon content.')
        else:
            sort_keys(sys.argv[2])
    elif cmd == 'sort':
        try:
            x = sys.argv[2]
        except IndexError:
            print('Usage: sort_keys sort [file]')
        else:
            sort_keys(x)
    elif cmd == 'pop':
        try:
            x = (sys.argv[2], sys.argv[3:])
        except IndexError:
            print('Usage: sort_keys pop [file] [keys]\n\n`keys` can be names or keys.')
        else:
            pop_keys(*x)
            print('List has been sorted.')
            sort_keys(x[0])
    else:
        print('Usage: sort_keys sort|pop|add {key(s)}')
