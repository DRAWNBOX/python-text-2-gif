from concurrent.futures import process
import os
from PIL import Image, ImageDraw, ImageFont
import re
import time

COLOR_TYPE = 'RGB'
WHITE = (255, 255, 255)
BLACK = (0,0,0)

IMAGE_SIZE = (500, 500)
TEXT_SIZE = (250,250)
FRAME_COUNT = 7
comicsans = ImageFont.truetype("comicbd.ttf", 100)

def make_frames(images, textinput, file_name):
    
    #Generates images of text in images array from text input
    start_time = time.time()
    for word in textinput:
        img = Image.new(COLOR_TYPE, IMAGE_SIZE, color=WHITE)
        draw = ImageDraw.Draw(img)
        draw.text(TEXT_SIZE, word, fill=BLACK,font=comicsans,anchor="mm", align='center')
        images.append(img)
        if word == textinput[len(textinput)-1]:
            for frame in range(FRAME_COUNT):
                images.append(img)

    processing_end_time = time.time()
    processing_time = processing_end_time - start_time

    gif_start_time = time.time()
    output_gif(images, file_name)
    gif_end_time = time.time()
    gif_creation_time = gif_end_time - gif_start_time

    total_time = gif_end_time -start_time

    print("Processing Time: " + str(processing_time) + " Seconds.")
    print("Gif Saving Time: " + str(gif_creation_time) + " Seconds.")
    print("Total Time: " + str(total_time) + " Seconds.")

def output_gif(images, file_name) -> None:
    
    #Creates gif frome image array and creates a file.
    if os.path.exists("./output_gif/"):
        images[0].save("./output_gif/" + file_name + ".gif", save_all=True, append_images=images[1:], optimize=False, duration=250, loop=0)

    else:
        os.mkdir("./output_gif/")
        images[0].save("./output_gif/" + file_name + ".gif", save_all=True, append_images=images[1:], optimize=False, duration=250, loop=0)

    

def openfile(file_path):
    
    #Opens file specified from path and returns its contents and name
    
    file_name = re.search("/[a-zA-Z]+\.txt", file_path).group()
    file_name = file_name[1:-4]
    print(file_name)
    with open(file_path, "r") as file:
        return [file.read().split(), file_name]