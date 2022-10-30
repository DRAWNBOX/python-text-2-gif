from PIL import Image, GifImagePlugin
import threading
import numpy as np

def multi_threaded_save(data, file_name):    
    data[0][0].save("./output_gif/" + file_name + ".gif", save_all=True, append_images=data[0][1:], optimize=False, duration=250, loop=0)
    print("")

def gif_combine(file_names):
    GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_AFTER_DIFFERENT_PALETTE_ONLY
    append_list = []
    for file in file_names:
        append_list.append(Image.open("./output_gif/" + file + ".gif"))
    file_name = file_names[0]
    print(append_list[0])
    append_list[0].save("./output_gif/" + file_name + ".gif", save_all=True, append_images=append_list, optimize=False, duration=250, loop=0)
    

def split_lists(input_list, number_of_splits):

    input_numpy = np.array(input_list, dtype=object)
    
    split_list = np.array_split(input_numpy, number_of_splits)
    return split_list


def save_gif(images,file_name, processes):
    split_images_list = split_lists(images, processes)
    count = 0
    threads = []
    data = []
    name_list = []
    for item in split_images_list:
        new_name = file_name + str(count)
        data.append([item,  new_name])
        name_list.append(new_name)
        threads.append(threading.Thread(target=multi_threaded_save, args=(data[count], new_name,)))
        count = count + 1

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    #gif_combine(name_list)
    print("Done")