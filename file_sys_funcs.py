import os


def get_dir_size(path='.'):
    dir_size = 0
    with os.scandir(path) as p:
        for entry in p:
            if entry.is_file():
                dir_size += entry.stat().st_size
            elif entry.is_dir():
                dir_size += get_dir_size(entry.path)
    return dir_size

def write_new_vol(path, size):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
        os.makedirs(f"{path}\\data")
    with open(f"{path}\\config.txt", "w") as f:
        f.write(str(size))
        f.close()
    with open(f"{path}\\buffer.bin", "wb") as f:
        f.seek(size - 1)
        f.write(b"\0")
        f.close()



def re_alloc_buffer(path):
    with open(f"{path}\\config.txt", "r") as f:
        allocated_space = int(f.read())
        f.close()
    used_space = get_dir_size(path)
    buffered_space = os.path.getsize(f"{path}\\buffer.bin")

    size = allocated_space - (used_space - buffered_space)
    with open(f"{path}\\buffer.bin", "wb") as f:
        f.seek(size - 1)
        f.write(b"\0")
        f.close()
