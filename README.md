# DentMamba

Official implementation of **DentMamba: An Anatomy-Aware Global-Local Hybrid Network for Large-Scale Multi-Class Dental Disease Detection**.

DentMamba is a two-stage framework for dental disease detection in panoramic radiographs. The first stage localizes tooth-level regions and generates anatomically meaningful tooth ROIs, while the second stage performs fine-grained dental disease detection within each cropped tooth region.

> The first-stage module is used for tooth localization rather than tooth numbering. It only requires each tooth region to be sufficiently covered by the cropped ROI. On 600 panoramic radiographs containing 17,591 tooth instances, the module detected 17,564 teeth at IoU=0.5, achieving a tooth-level detection rate of 99.8%, suggesting that the first-stage error has a negligible impact on the subsequent detection stage.

---

## Highlights

- Two-stage global-to-local dental disease detection framework.
- Anatomy-aware modeling for dental structures with strong vertical anisotropy.
- Global-local hybrid feature representation for subtle dental disease detection.
- Scale-adaptive loss design for small and scale-varied targets.
- Support for training, validation, inference, Grad-CAM visualization, FPS evaluation, COCO-style metrics, ERF visualization, and model export.

---

## Framework

The overall framework of DentMamba consists of two stages:

1. **Global Tooth Localization**  
   The first stage identifies tooth-level regions from the panoramic radiograph and generates cropped tooth ROIs.

2. **Local Dental Disease Detection**  
   The second stage performs fine-grained disease detection within each localized tooth ROI and maps the predicted boxes back to the original panoramic radiograph.

<!-- Replace the following path with your actual framework figure if needed. -->
<!-- ![DentMamba Framework](assets/framework.png) -->

---

## Dataset

We collected **20,000 high-resolution panoramic radiographs** from a clinical partner. The image resolution is **2610 × 1560**. The annotation quality was controlled through a hierarchical review process involving **8 annotators, 3 auditors, and 1 expert**, with multi-round quality checks and a 90% acceptance threshold. For experiments, **18,534 validated images** were used for model training and evaluation via K-fold cross-validation.

The dataset covers **12 clinically relevant dental disease categories**, including both disease-related abnormalities and treatment-associated radiographic findings commonly observed in dental diagnosis.

| ID | Category |
|---:|---|
| 0 | Impacted tooth |
| 1 | Implant |
| 2 | Fixed bridge |
| 3 | Crown restoration |
| 4 | Filling |
| 5 | Root canal filling |
| 6 | Caries |
| 7 | Dental calculus |
| 8 | Post-and-core restoration |
| 9 | Residual crown |
| 10 | Residual root |
| 11 | Periapical periodontitis |

Due to privacy and institutional restrictions on clinical radiographs, the full dataset cannot be publicly released at this stage. This repository provides the implementation, evaluation scripts, category definitions, and usage instructions to support reproducibility.

---

## Environment

The experiments were conducted with the following environment:

| Package | Version |
|---|---|
| Python | 3.10.14 |
| PyTorch | 2.2.2+cu121 |
| TorchVision | 0.17.2+cu121 |
| CUDA | 12.1 |
| timm | 1.0.7 |
| mmcv | 2.2.0 |
| mmengine | 0.10.4 |

We recommend creating a new conda environment:

```bash
conda create -n dentmamba python=3.10.14
conda activate dentmamba
```

Install PyTorch with CUDA 12.1:

```bash
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121
```

Install other required packages:

```bash
pip install -r requirements.txt
```

Install OpenMMLab dependencies:

```bash
pip install -U openmim
mim install mmengine==0.10.4
mim install "mmcv==2.2.0"
```

If an official `ultralytics` package has been installed previously, please uninstall it to avoid conflicts with the modified local implementation:

```bash
pip uninstall -y ultralytics
```

---

## Repository Structure

```text
Dent_Mamba/
├── dataset/
│   └── split_data.py          # Dataset splitting script
├── ultralytics/               # Modified local detection framework
├── train.py                   # Model training script
├── val.py                     # Model validation script
├── detect.py                  # Inference script
├── heatmap.py                 # Grad-CAM visualization script
├── get_FPS.py                 # Model size, inference time, and FPS calculation
├── get_COCO_metrice.py        # COCO-style metric calculation
├── plot_result.py             # Training and validation curve visualization
├── get_model_erf.py           # Effective receptive field visualization
├── export.py                  # Model export script
├── requirements.txt           # Python dependencies
└── README.md
```

---

## Usage

### 1. Dataset Preparation

Split the dataset into training and testing subsets:

```bash
python dataset/split_data.py
```

Please make sure that the dataset path and category configuration are correctly set before running this script.

### 2. Training

Train DentMamba:

```bash
python train.py
```

Training settings such as dataset path, input size, batch size, number of epochs, and model configuration can be modified in the corresponding configuration file or directly in `train.py`.

### 3. Validation

Evaluate a trained model:

```bash
python val.py
```

This script is used to calculate the main detection metrics on the validation or test set.

### 4. Inference

Run inference on panoramic radiographs:

```bash
python detect.py
```

The detection results will be saved to the specified output directory.

### 5. Grad-CAM Visualization

Generate Grad-CAM heatmaps:

```bash
python heatmap.py
```

This script visualizes the regions that contribute most to the model predictions.

### 6. FPS and Model Complexity

Calculate model storage size, inference time, and FPS:

```bash
python get_FPS.py
```

This script is used to evaluate the computational efficiency of the model.

### 7. COCO-Style Evaluation

Compute COCO-style detection metrics:

```bash
python get_COCO_metrice.py
```

### 8. Training Curve Visualization

Plot training and validation curves:

```bash
python plot_result.py
```

### 9. Effective Receptive Field Visualization

Visualize the effective receptive field of the model:

```bash
python get_model_erf.py
```

### 10. Model Export

Export the trained model:

```bash
python export.py
```

The exported model can be used for deployment or further evaluation.

---

## Running Pipeline

For convenience, the main scripts are summarized below:

| Step | Script | Description |
|---:|---|---|
| 1 | `dataset/split_data.py` | Split the dataset into training and testing subsets |
| 2 | `train.py` | Train the DentMamba model |
| 3 | `val.py` | Evaluate the trained model |
| 4 | `detect.py` | Perform inference on panoramic radiographs |
| 5 | `heatmap.py` | Generate Grad-CAM visualization results |
| 6 | `get_FPS.py` | Calculate model size, inference time, and FPS |
| 7 | `get_COCO_metrice.py` | Compute COCO-style detection metrics |
| 8 | `plot_result.py` | Plot training and validation curves |
| 9 | `get_model_erf.py` | Visualize the effective receptive field |
| 10 | `export.py` | Export the trained model |

---

## Notes

- The local `ultralytics/` directory contains modified components used by DentMamba. Please avoid installing or importing another incompatible version of `ultralytics`.
- The dataset is not included in this repository due to privacy restrictions.
- Please update dataset paths and model configuration files according to your local environment before training or evaluation.
- If CUDA, PyTorch, MMCV, or MMEngine version conflicts occur, reinstall PyTorch first and then reinstall OpenMMLab dependencies through `mim`.

---

## Citation

If this repository is helpful for your research, please cite our work:

```bibtex
@inproceedings{dentmamba2026,
  title     = {DentMamba: An Anatomy-Aware Global-Local Hybrid Network for Large-Scale Multi-Class Dental Disease Detection},
  author    = {Zhang Kang and Zhuang Shaojie and Wei Guangshun and Zhou Yuanfeng},
  booktitle = {},
  year      = {2026}
}
```

---

## Acknowledgement

This repository is built upon open-source object detection frameworks and related deep learning libraries. We thank the authors and contributors of these projects for their valuable work.
