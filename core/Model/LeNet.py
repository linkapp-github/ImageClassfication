import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Activation, Flatten, Dense
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import multi_gpu_model

#參考 https://blog.csdn.net/wmy199216/article/details/71171401
def buildLeNetModel(img_height, img_width, img_channl, num_classes, num_GPU):
    inputs = (img_height, img_width, img_channl)
    model = Sequential()

    model.add(Conv2D(32, (5, 5), strides = (1, 1), padding = 'valid', activation = 'relu', input_shape = inputs))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Conv2D(64, (5, 5), strides = (1, 1), padding = 'valid', activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation = 'relu'))
    model.add(Dense(num_classes, activation = 'softmax'))

    model.summary()    
    if(num_GPU > 1):
        model = multi_gpu_model(model, gpus = num_GPU)
    model.compile(loss = categorical_crossentropy,
              optimizer = Adam(lr = 0.001),
              metrics = ['accuracy'])
    return model
