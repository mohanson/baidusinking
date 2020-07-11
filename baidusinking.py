import os.path
import subprocess


def get_current_index() -> int:
    with open('res/i', 'r') as f:
        return int(f.read(), 16)


def inc_current_index():
    s = hex(get_current_index() + 1)[2:]
    s = f'{s:0>8}'
    with open('res/i', 'w') as f:
        f.write(s)


if not os.path.exists('res'):
    os.mkdir('res')
    with open('res/i', 'w') as f:
        f.write('00000000')

for _ in range(1 << 32):
    next_index = hex(get_current_index() + 1)[2:]
    next_index = f'{next_index:0>8}'
    subprocess.call(f'cat /dev/urandom | head -c 67108864 > res/{next_index}.zip', shell=True)
    subprocess.call(f'BaiduPCS-Go upload res/{next_index}.zip /肥大', shell=True)
    subprocess.call(f'rm res/{next_index}.zip', shell=True)
    inc_current_index()
