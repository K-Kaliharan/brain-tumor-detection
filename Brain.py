# Source of Data
print("Dataset Name: Brain Tumor MRI Dataset")
print("Source: Kaggle - Brain Tumor MRI Dataset (Figshare, SARTAJ, Br35H)")
print("Format: Image dataset (.jpg), organized in class-labeled folders")

#Number of Records/Samples
import os

TRAIN_DIR = "archive/Training"
TEST_DIR ="archive/Testing"

classes = sorted(os.listdir(TRAIN_DIR))
total_train = sum(len(os.listdir(os.path.join(TRAIN_DIR, c))) for c in classes)
total_test = sum(len(os.listdir(os.path.join(TEST_DIR, c))) for c in classes)

print("Total Training Samples:", total_train)
print("Total Testing Samples:", total_test)
print("Total Samples:", total_train + total_test)

for c in classes:
    print(c, "-> Train:", len(os.listdir(os.path.join(TRAIN_DIR, c))), "Test:", len(os.listdir(os.path.join(TEST_DIR, c))))

#Features/Attributes
import os
import cv2

TRAIN_DIR = "archive/Training"
classes = sorted(os.listdir(TRAIN_DIR))

sample_img = os.path.join(TRAIN_DIR, classes[0], os.listdir(os.path.join(TRAIN_DIR, classes[0]))[0])
img = cv2.imread(sample_img)

print("Image Width:", img.shape[1])
print("Image Height:", img.shape[0])
print("Channels:", img.shape[2])
print("Classes (Labels):", classes)

#Training and Testing Split
import os

TRAIN_DIR = "archive/Training"
TEST_DIR = "archive/Testing"


classes = sorted(os.listdir(TRAIN_DIR))
total_train = sum(len(os.listdir(os.path.join(TRAIN_DIR, c))) for c in classes)
total_test = sum(len(os.listdir(os.path.join(TEST_DIR, c))) for c in classes)
total = total_train + total_test

print("Training Samples:", total_train, "(", round(total_train/total*100, 2), "% )")
print("Testing Samples:", total_test, "(", round(total_test/total*100, 2), "% )")

#Data Format/Type
print("Data Type: Unstructured Image Data")
print("File Format: .jpg")
print("Label Type: Folder-based class labels")