from glob import glob

import cv2
import numpy as np
from scipy import misc
from tensorflow import keras


class ModelGenerator:
    @staticmethod
    def load_images(image_dir: str):
        images = [cv2.imread(bottle_image) for bottle_image in glob(f"/{image_dir}/*")]

        images = [image for image in images if image is not None]

        for index, image in enumerate(images):
            images[index] = misc.imresize(image, (100, 100, 3))

        images = np.array(images)
        images = images / images.max()
        np.random.shuffle(images)

        train_images_count = int(len(images) * 0.8)
        return images[:train_images_count], images[train_images_count:]

    def prepare_model(self, bottles_dir: str, glasses_dir: str):
        bottles_train_data, bottles_test_data = self.load_images(bottles_dir)
        glasses_train_data, glasses_test_data = self.load_images(glasses_dir)

        bottles_train_labels, bottles_test_labels = np.zeros(len(bottles_train_data)), np.zeros(len(bottles_test_data))
        glasses_train_labels, glasses_test_labels = np.ones(len(glasses_train_data)), np.ones(len(glasses_test_data))

        train_data = np.vstack((bottles_train_data, glasses_train_data))
        test_data = np.vstack((bottles_test_data, glasses_test_data))

        train_labels = np.hstack((bottles_train_labels, glasses_train_labels))
        test_labels = np.hstack((bottles_test_labels, glasses_test_labels))

        train_permutation = np.random.permutation(len(train_data))
        test_permutation = np.random.permutation(len(test_data))

        train_data, train_labels = train_data[train_permutation], train_labels[train_permutation]
        test_data, test_labels = test_data[test_permutation], test_labels[test_permutation]

        model = keras.Sequential([
            keras.layers.Conv2D(30, 5, activation=keras.activations.relu, input_shape=(100, 100, 3)),
            keras.layers.AveragePooling2D((3, 3)),
            keras.layers.Conv2D(30, 5, activation=keras.activations.relu),
            keras.layers.AveragePooling2D(),
            keras.layers.Dropout(0.5),
            keras.layers.Conv2D(10, 5, activation=keras.activations.relu),
            keras.layers.AveragePooling2D(),
            keras.layers.Flatten(),
            keras.layers.Dense(30, activation=keras.activations.sigmoid),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(2, activation=keras.activations.softmax),
        ])

        model.compile(keras.optimizers.Adam(),
                      keras.losses.sparse_categorical_crossentropy,
                      ["accuracy"])

        model.fit(train_data, train_labels, epochs=100, validation_data=(test_data, test_labels))
