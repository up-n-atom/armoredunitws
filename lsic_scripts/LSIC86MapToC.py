import os

_src_dir_fd = None

src_path = os.path.join(os.path.pardir, 'src')


def src_file_opener(path, flags):
    global _src_dir_fd

    if _src_dir_fd is not None:
        return os.open(path, flags, mode=0o644, dir_fd=_src_dir_fd)
    else:
        return os.open(path, flags)

def src_file_exists(path, ignore_errors=True):
    global _src_dir_fd

    try:
        return os.lstat(path, dir_fd=_src_dir_fd) is not None
    except FileNotFoundError:
        if ignore_errors:
            return False
        raise

def hex_or_str(s):
    try:
        if not s.endswith('H'):
            raise ValueError
        return int(s[:-1], 16)
    except ValueError:
        return s

def ptr_or_str(s):
    try:
        segment, offset = [int(x, 16) for x in s.split(':')]
        return (segment << 4) + offset
    except ValueError:
        return s.removesuffix('_')

def read_and_map(file, keys, function):
    for line in file:
        if not (values := line.split()):
            break
        yield dict(zip(keys, map(function, values), strict=True))

def create_c_file(file_name):
    try:
        with open(f"{file_name}.c", 'x', opener=src_file_opener) as file:
            pass
    except:
        pass

def write_far_data_to_file(file_name, var_name):
    try:
        src_file_exists(file_name, ignore_errors=False)

        with open(file_name, 'a', newline='\r\n', opener=src_file_opener) as file:
             raise NotImplementedError
    except IOError:
        pass

def convert_to_src(segments, publics):
    for segment in segments:
        match segment['name'][-4:], segment['class']:
            case ['TEXT', 'CODE']:
                # C:/LSIJ/LSIC86pv/LSIC86MAN/chapter6x.doc
                # For example, when the program in the file foo.c is compiled using the P model,
                # it is placed in the segment named foo_TEXT
                create_c_file(segment['name'][:-5])
            case ['DATA', 'FAR_DATA']:
                pass

def read_map_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match line.lower().split():
                case ['start', *_] as keys:
                    segments = [segment for segment in read_and_map(file, keys, hex_or_str) if segment['class'] in ('CODE', 'FAR_DATA')]
                case ['address', *_]:
                    next(file) # hack
                    publics = [_ for _ in read_and_map(file, ('address', 'name'), ptr_or_str)]
    return segments, publics

def main():
    global _src_dir_fd

    try:
        os.makedirs(src_path)
    except FileExistsError:
        pass
    finally:
        if _src_dir_fd is None:
            _src_dir_fd = os.open(src_path, os.O_RDONLY)

    try:
        convert_to_src(*read_map_file(os.path.join(os.path.pardir, 'ArmoredUnit.MAP')))
    except:
        pass

    if _src_dir_fd is not None:
        os.close(_src_dir_fd)


if __name__ == '__main__':
    main()
