import os.path
import subprocess


def get_current_index() -> int:
    with open('res/i', 'r') as f:
        return int(f.read(), 16)


def inc_current_index():
    s = hex(get_current_index() + 1)[2:]
    s = f'{s:0>4}'
    with open('res/i', 'w') as f:
        f.write(s)


if not os.path.exists('res'):
    os.mkdir('res')
    with open('res/i', 'w') as f:
        f.write('0000')


next_index = hex(get_current_index() + 1)[2:]
next_index = f'{next_index:0>4}'

subprocess.call(f'cat /dev/urandom | head -c 1073741824 > res/{next_index}.zip', shell=True)
subprocess.call(f'BaiduPCS-Go upload --nosplit res/{next_index}.zip /肥大', shell=True)
subprocess.call(f'rm res/{next_index}.zip')
