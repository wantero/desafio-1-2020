import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from os import listdir
from os.path import isfile, join

INPUT_PATH  = "./doc/source/dataset/v3/negative/"
OUTPUT_PATH = "./doc/source/dataset/v3/negative/output/"

onlyfiles = [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]

print(len(onlyfiles))

for file in onlyfiles:
    print(INPUT_PATH + file)

    # definir caminhos da imagem original e diretório do output
    IMAGE_PATH = INPUT_PATH + file    
    
    # carregar a imagem original e converter em array
    image = load_img(IMAGE_PATH)
    image = img_to_array(image)
    
    # adicionar uma dimensão extra no array
    image = np.expand_dims(image, axis=0)
    
    # criar um gerador (generator) com as imagens do
    # data augmentation
    imgAug = ImageDataGenerator(rotation_range=45, width_shift_range=0.1,
                                height_shift_range=0.1, zoom_range=0.25,
                                fill_mode='nearest', horizontal_flip=True)
    imgGen = imgAug.flow(image, save_to_dir=OUTPUT_PATH,
                        save_format='jpg', save_prefix='img_')
    
    # gerar 10 imagens por data augmentation
    counter = 0
    for (i, newImage) in enumerate(imgGen):
        counter += 1
    
        # ao gerar 10 imagens, parar o loop
        if counter == 3:
            break