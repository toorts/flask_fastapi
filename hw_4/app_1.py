import os
import time
import threading
from pathlib import Path
import requests


task_dir = os.path.join(Path(__file__).resolve().parent, 'images')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'threads')

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

urls = [
    'https://i0.wp.com/modogeeks.com/wp-content/uploads/2016/05/r2d2.png',
    'https://images.squarespace-cdn.com/content/v1/55492cebe4b0e926e58cd00f/1450923381371-B4L76S2L5KX8ZID20C5R/R2D2_low.jpg',
    'https://images.bauerhosting.com/legacy/media/5d72/5e04/ddd8/9ce2/65de/cd3a/star-wars-r2-d2-tall-image.jpg',
    'https://cdn.theatlantic.com/thumbor/AO54tap7Ro8Wt1DhcWEqBK-O9rE=/0x40:1000x603/976x549/media/img/mt/2015/12/MV5BOTcwMTg0NDcxMl5BMl5BanBnXkFtZTcwMjEyMTIyMw._V1_SX1224_SY560_-2/original.jpg',
    'https://super.abril.com.br/wp-content/uploads/2016/09/super_imgc-3po_e_r2-d2.jpg',
    'https://media.wired.co.uk/photos/606da2976a2b7484dab92f59/16:9/w_1920,h_1080,c_limit/star-wars-force-awakens-r2d2.jpg',
]


def download_image(url: str):
    response = requests.get(url)
    paths = url.replace('https://', '').split('/')
    dirname, filename = paths[0].replace('.', '_'), paths[-1]

    if not os.path.exists(os.path.join(BASE_DIR, dirname)):
        os.mkdir(os.path.join(BASE_DIR, dirname))

    with open(os.path.join(BASE_DIR, dirname, filename), 'wb') as f:
        f.write(response.content)


threads: list[threading.Thread] = []

start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_image, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Completed download in {time.time() - start_time} seconds.')