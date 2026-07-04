from ultralytics import YOLO
import torch
import config


def main():
    print("CUDA:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print(torch.cuda.get_device_name(0))

    model = YOLO(config.MODEL)

    model.train(
    data=str(config.DATASET),
    epochs=config.EPOCHS,
    imgsz=config.IMAGE_SIZE,
    batch=config.BATCH_SIZE,
    workers=config.WORKERS,
    device=config.DEVICE,
    project=config.PROJECT,
    name=config.RUN_NAME,
    cache=config.CACHE,     
    seed=config.SEED,
)


if __name__ == "__main__":
    main()