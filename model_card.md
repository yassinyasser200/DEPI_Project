# Model Card – Drone-SAR Person Detection

## Model Overview

- **Model:** YOLOv8m
- **Framework:** Ultralytics YOLOv8
- **Task:** Person Detection for Search and Rescue (SAR)
- **Dataset:** Merged SAR Drone Dataset
- **Classes:** 1 (person)

---

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Model | YOLOv8m |
| Image Size (Baseline) | 640 × 640 |
| Optimizer | AdamW (Auto) |
| Epochs | 20 (Baseline), 15 (Ablation Studies) |
| Batch Size | 8 |
| Device | NVIDIA GPU |
| Seed | 42 |

---

## Baseline Performance

| Metric | Value |
|--------|------:|
| Precision | 0.837 |
| Recall | 0.725 |
| mAP@0.5 | 0.781 |
| mAP@0.5:0.95 | 0.395 |

---

## Ablation Studies

| Experiment | Configuration | mAP@0.5 | mAP@0.5:0.95 |
|------------|--------------|---------:|-------------:|
| Baseline | 640 × 640 | 0.781 | 0.395 |
| Resolution | 1280 × 1280 | **0.796** | **0.424** |
| No Augmentation | Augmentation Disabled | 0.742 | 0.415 |
| Hyperparameter Tuning | Lower Learning Rate | 0.755 | 0.371 |
| TinyPerson-style Augmentation | Scale + Mosaic + Copy-Paste | 0.718 | 0.344 |

---

## Key Findings

- Increasing the input resolution from **640 to 1280** achieved the best detection performance.
- Disabling augmentation reduced mAP@0.5 compared to the baseline.
- The tested hyperparameter adjustment did not improve overall performance.
- The TinyPerson-style augmentation configuration used in this project did not improve detection performance on the merged dataset.

---

## Best Configuration

- **Model:** YOLOv8m
- **Input Resolution:** 1280 × 1280
- **Best mAP@0.5:** 0.796
- **Best mAP@0.5:0.95:** 0.424

---

## Project Outputs

- Trained YOLOv8 model weights (`best_sar.pt`)
- Training logs
- Ablation study results
- Training configuration
- Reproducible training script

---

## Limitations

- Experiments were limited by available GPU resources and training time.
- Results may be further improved through longer training, additional hyperparameter optimization, or larger datasets.

---

## Environment

- Python 3.12
- PyTorch
- Ultralytics YOLOv8
- CUDA-enabled NVIDIA GPU