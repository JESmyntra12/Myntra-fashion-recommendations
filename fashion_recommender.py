# -*- coding: utf-8 -*-
"""Fashion_recommender.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JZmNvpSIr7REjdcOuYRlr1N9-Bk9rFMJ
"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

pip install kaggle

!kaggle datasets download -d paramaggarwal/fashion-product-images-small

pip install tensorflow

import zipfile

# Unzip the dataset
with zipfile.ZipFile("/content/fashion-product-images-small.zip", 'r') as zip_ref:
    zip_ref.extractall("/content/fashion-product-images-small")





# import zipfile
# import numpy as np
# import os
# import cv2
# from tqdm import tqdm
# from sklearn.neighbors import NearestNeighbors
# from tensorflow.keras.applications import ResNet50
# from tensorflow.keras.applications.resnet50 import preprocess_input


# # Load the dataset
# data_path = "/content/fashion-product-images-dataset/fashion-dataset/fashion-dataset/images"

# def preprocess_image(image_path):
#     img = cv2.imread(image_path)
#     if img is None:
#         print(f"Warning: Unable to load image from path: {image_path}. Skipping...")
#         return None
#     img = cv2.resize(img, (224, 224))
#     img = preprocess_input(img)
#     return img

# # Load and preprocess all images in the dataset
# images = []
# image_paths = [os.path.join(data_path, img) for img in os.listdir(data_path)]
# for img_path in tqdm(image_paths):
#     img = preprocess_image(img_path)
#     if img is not None:
#         images.append(img)

# # Convert the list of images to a numpy array
# images = np.array(images)

# # Feature extraction using ResNet50
# resnet_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
# image_features = resnet_model.predict(images)

# # Train Nearest Neighbors model
# nn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
# nn_model.fit(image_features)

import zipfile
import numpy as np
import os
import cv2
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

# # Unzip the dataset
# with zipfile.ZipFile("/content/fashion-product-images-dataset.zip", 'r') as zip_ref:
#     zip_ref.extractall("/content/fashion-product-images-dataset")

# Load the dataset
data_path = "/content/fashion-product-images-small/images"

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Warning: Unable to load image from path: {image_path}. Skipping...")
        return None
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    return img

# Load and preprocess all images in the dataset
images = []
image_paths = [os.path.join(data_path, img) for img in os.listdir(data_path)]
for img_path in image_paths:
    img = preprocess_image(img_path)
    if img is not None:
        images.append(img)

# Convert the list of images to a numpy array
images = np.array(images)

# Feature extraction using ResNet50
resnet_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
image_features = resnet_model.predict(images)

# Train Nearest Neighbors model
nn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
nn_model.fit(image_features)

# # Recommendation function
# def recommend_products(image_path):
#     input_image = preprocess_image(image_path)
#     if input_image is None:
#         return []
#     input_features = resnet_model.predict(np.expand_dims(input_image, axis=0))
#     distances, indices = nn_model.kneighbors(input_features)
#     return [image_paths[i] for i in indices[0]]

# # Test the recommendation function
# test_image_path = "/content/fashion-product-images-dataset/fashion-dataset/fashion-dataset/images/test_image.jpg"
# suggested_images = recommend_products(test_image_path)
# print("Suggested Image Paths:", suggested_images)

# # Evaluation (Optional)
# # Evaluate the accuracy of the recommendation system using appropriate metrics
# # This could involve collecting user feedback and measuring the relevance of recommendations

def recommend_products(image_path):
    input_image = preprocess_image(image_path)
    if input_image is None:
        return []
    input_features = resnet_model.predict(np.expand_dims(input_image, axis=0))
    distances, indices = nn_model.kneighbors(input_features)
    return [image_paths[i] for i in indices[0]]

# Test the recommendation function
test_image_path = "/content/download.jpg"
suggested_images = recommend_products(test_image_path)
print("Suggested Image Paths:", suggested_images)

from IPython.display import Image, display, HTML


# Test the recommendation function
test_image_path = "/content/download.jpg"
suggested_images = recommend_products(test_image_path)

print("Uploaded Test Image:")
display(Image(filename=test_image_path, width=100, height=100))
print("\n")
# Display the suggested images
print("Suggestions you may follow :")
for image_path in suggested_images:
    display(Image(filename=image_path, width=100, height=100))

from google.colab import drive
drive.mount('/content/drive')

# Save the trained model to Google Drive
model_save_path = "/content/drive/My Drive/saved_model/resnet_model"
resnet_model.save(model_save_path)
print("Model saved successfully at:", model_save_path)