# Drone-SAR: Person Detection for Search and Rescue using YOLOv8

## Overview

This project develops a person detection model for Search and Rescue (SAR) scenarios using **YOLOv8**. The objective is to accurately detect people in aerial drone imagery by training and evaluating different model configurations on a merged SAR dataset.

The project includes baseline training, multiple ablation studies, hyperparameter tuning, and TinyPerson-style augmentation experiments.

---

## Model

- **Architecture:** YOLOv8m
- **Framework:** Ultralytics YOLOv8
- **Task:** Object Detection
- **Class:** Person

---

## Dataset

The model was trained on a merged drone-based SAR dataset.

Dataset structure:

```
final_dataset/
│
├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
│
└── data.yaml
```

> **Note:** The dataset is not included in this repository due to its large size.

---

## Project Structure

```
Drone-SAR/

├── scripts/
│   ├── train.py
│   └── verify_dataset.py
│
├── training_runs/
│   ├── baseline/
│   ├── ablation_noaug/
│   ├── ablation_hyperparam/
│   └── ablation_tinyperson/
│
├── weights/
│   
│
├── config.py
├── model_card.md
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Drone-SAR.git
cd Drone-SAR
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Training

Run training using:

```bash
python scripts/train.py
```

---

## Experiments

The following experiments were conducted:

| Experiment | Description |
|------------|-------------|
| Baseline | YOLOv8m, 640×640 |
| Ablation 1 | Resolution 1280×1280 |
| Ablation 2 | Augmentation Disabled |
| Ablation 3 | Hyperparameter Tuning |
| TinyPerson | TinyPerson-style Augmentation |

---

## Results

| Experiment | mAP@0.5 | mAP@0.5:0.95 |
|------------|---------:|-------------:|
| Baseline | 0.781 | 0.395 |
| Resolution 1280 | **0.796** | **0.424** |
| No Augmentation | 0.742 | 0.415 |
| Hyperparameter Tuning | 0.755 | 0.371 |
| TinyPerson Augmentation | 0.718 | 0.344 |

Increasing the input resolution to **1280×1280** achieved the best detection performance among all evaluated configurations.

---

## Deliverables

- YOLOv8 trained weights (`best_sar.pt`)
- Training logs
- Ablation study results
- Model Card
- Reproducible training script

---

## Requirements

- Python 3.12
- PyTorch
- Ultralytics
- CUDA-enabled NVIDIA GPU (recommended)

---

## Authors

Faculty of Computers and Artificial Intelligence

Helwan University

Drone Search and Rescue Project