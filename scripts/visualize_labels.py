import random
from pathlib import Path

import cv2

DATASET_PATH = Path(r"C:\Users\ASUS\Downloads\Drone-SAR\final_dataset")

IMAGE_DIR = DATASET_PATH / "images" / "train"
LABEL_DIR = DATASET_PATH / "labels" / "train"

images = list(IMAGE_DIR.glob("*.jpg"))
images += list(IMAGE_DIR.glob("*.png"))
images += list(IMAGE_DIR.glob("*.jpeg"))

sample = random.sample(images, 5)

for image_path in sample:

    image = cv2.imread(str(image_path))
    h, w = image.shape[:2]

    label_path = LABEL_DIR / (image_path.stem + ".txt")

    if label_path.exists():

        with open(label_path) as f:

            for line in f.readlines():

                cls, xc, yc, bw, bh = map(float, line.split())

                x1 = int((xc - bw/2) * w)
                y1 = int((yc - bh/2) * h)

                x2 = int((xc + bw/2) * w)
                y2 = int((yc + bh/2) * h)

                cv2.rectangle(image,
                              (x1, y1),
                              (x2, y2),
                              (0,255,0),
                              2)

    cv2.imshow(image_path.name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()