import imageio.v2 as imageio
import os

file_list = sorted(os.listdir('img'))
IMAGES = []
for file_name in file_list:
    file_path = os.path.join('img', file_name)
    image = imageio.imread(file_path)
    IMAGES.append(image)

duration_per_frame = 200 

imageio.mimsave('snake.gif', IMAGES, loop=0, duration=duration_per_frame)