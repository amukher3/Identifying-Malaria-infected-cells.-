# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 04:04:35 2020

@author: abhi0
"""

#CNN augmented with Image Data generator model

#Building the CNN
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.regularizers import l2
from keras import optimizers
from keras.layers import Dropout
from keras import initializers
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator


# Defining the model -- CNN
classifier = Sequential()


#image_dims:
hor_dim=64
Ver_dim=64

#Convolution
classifier.add(Conv2D(128,(3, 3),strides=4, input_shape = (hor_dim,Ver_dim, 3), activation = 'relu'))

#Pooling for the first layer:
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer:
classifier.add(Conv2D(128, (3, 3), activation = 'relu'))

#Pooling for the seconds layer:
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#Dropout:
Dropout(rate=0.4)

#Flattening
classifier.add(Flatten())

classifier.add(Dense(activity_regularizer=l2(0.001),units=128,activation = 'relu'))
initializers.he_normal(seed=42)
classifier.add(Dense(units = 1,activation ='sigmoid'))

#Compiling the CNN
adam_opt=optimizers.Adam(learning_rate=0.001,beta_1=0.9, beta_2=0.99, amsgrad=True)
classifier.compile(optimizer =adam_opt, loss = 'binary_crossentropy', metrics = ['accuracy'])

##Checkpoint:
checkpoint=ModelCheckpoint(filepath='C:/Users/abhi0/OneDrive/Documents/Kaggle_Malaria_cell_image_dataset/best_model.h5', monitor='val_loss', save_best_only=True)

train_datagen = ImageDataGenerator(rescale = 1./255,
                                  shear_range = 0.2,
                                  zoom_range = 0.2,
                                  horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(
                            'C:/Users/abhi0/OneDrive/Documents/Kaggle_Malaria_cell_image_dataset/cell_images/Training_set',
                             target_size = (hor_dim, Ver_dim),
                             batch_size = 50,
                             class_mode = 'binary')

test_set = test_datagen.flow_from_directory(
                            'C:/Users/abhi0/OneDrive/Documents/Kaggle_Malaria_cell_image_dataset/cell_images/Test_set',
                             target_size = (hor_dim, Ver_dim),
                             batch_size = 50,
                             class_mode = 'binary')

history=classifier.fit_generator(training_set,
                         steps_per_epoch =22683,
                         epochs =5,
                         validation_data = test_set,
                         validation_steps =4937,
                         callbacks=[checkpoint])


#Printing history:
print(history.history.keys())

#Accuracy history:
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'])
plt.show()


