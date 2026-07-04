from pathlib import Path

DATASET_PATH = Path(r"C:\Users\ASUS\Downloads\Drone-SAR\final_dataset")

splits = ["train", "val", "test"]

for split in splits:
    image_dir = DATASET_PATH / "images" / split
    label_dir = DATASET_PATH / "labels" / split

    images = list(image_dir.glob("*.jpg"))
    images += list(image_dir.glob("*.png"))
    images += list(image_dir.glob("*.jpeg"))

    labels = list(label_dir.glob("*.txt"))

    print(f"\n========== {split.upper()} ==========")
    print(f"Images : {len(images)}")
    print(f"Labels : {len(labels)}")

    image_names = {img.stem for img in images}
    label_names = {lbl.stem for lbl in labels}

    missing_labels = image_names - label_names
    missing_images = label_names - image_names

    print(f"Images without labels : {len(missing_labels)}")
    print(f"Labels without images : {len(missing_images)}")