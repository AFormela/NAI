# Autorzy: Aleksandra Formela s17402 i Michał Kosiński s16497
# Opis problemu: Uczenie sieci neuronowej rozpoznawać zwierzęta
# Źródlo danych: Cifar10

# Instrukcja przygotowania środowiska:
# 1. Upewniamy się, że posiadamy 64-bitową wersję Pythona 3.8.0
# 2. Używamy konsoli systemowej i wpsiujemy w niej komendę: python -m pip install tensorflow
# Do uruchomienia programu wykorzystujemy komendę w terminalu: python cifar-10_different_size.py


import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Preparing sets from cifar10 data set
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Dividing of image sets to 140
train_images, test_images = train_images / 140.0, test_images / 140.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Building model and layers
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(20))

# Model optimalization
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Model training
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# Evaluation and prediction
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print("Accuracy", test_acc)