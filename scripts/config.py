from pathlib import Path

DATASET = Path(r"C:\Users\ASUS\Downloads\Drone-SAR\final_dataset\data.yaml")

MODEL = "yolov8m.pt"

EPOCHS = 15
IMAGE_SIZE = 1280
BATCH_SIZE = 4

DEVICE = 0

PROJECT = "training_runs"
RUN_NAME = "ablation_res1280"

WORKERS = 4
SEED = 42

CACHE = "disk"         