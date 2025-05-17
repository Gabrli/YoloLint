# YOLO Dataset Debugger - ( YoloLint )

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/Apache-License-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![YOLO](https://img.shields.io/badge/YOLO-Dataset-yellow)
![Linting](https://img.shields.io/badge/Linting-PEP8-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-success)

---

## 🚀 About

**YoloLint** it's a tool to automatic dataset structure and annotation validation in YOLO. This tool can catch a typical errors in structure of directories, YAML files and annotation files, before you'll start model training.

---

## 📦 Structure of directories

```
.
├── yololint/
│   ├── clis/
│   │   ├── structure_validator_cli.py
│   │   └── annotation_checker.py
│   ├── structure_validator.py
│   ├── annotation_checker.py
│   ├── utils/
│   │   ├── compare_validate.py
│   │   └── add_file_to_list.py
│   └── constants/
│       └── folders.py
├── tests/
│   ├── test_structure_validator.py
│   ├── test_annotation_checker.py
│   └── utils/
│       └── prepare_lib_proccess.py
├── requirements.txt
├── setup.py
├── README.md
```
---

## 🛠️ Installation

```bash
pip install yololint
```

---

## ⚡ Quick Start

### ✅ Structure Validation

```python
from yololint.structure_validator import StructureValidator
import os

dataset_path = os.path.join(os.path.dirname(__file__), 'dataset')
checker = StructureValidator(dataset_path)
result = checker.dataset_validation()
print(result)
```

### ✅ Annotation validation

```python
from yololint.annotation_checker import AnnotationChecker
import os

labels_path = os.path.join(os.path.dirname(__file__), 'dataset', 'labels')
checker = AnnotationChecker(labels_path, liczba_klas)
print(checker.annotation_checker())
```

---

## 📝 Example of `data.yaml`

```yaml
names: ['class1', 'class2', 'class3']
nc: 3
```

---

## 🖥️ Available Terminal Scripts

After the installation package you can use this commends:
### Dataset Structure Validation

```sh
yololint-structure-v <path_to_folder_with_data>
```
**Example**
```sh
yololint-structure-v ./my_yolo_dataset
```

---

### File Annotation validation

```sh
yololint-annotation-v <path_to_folder_with_labels> <num_of_classes>
```
**Example:**
```sh
yololint-annotation-v ./my_yolo_dataset/labels 3
```

---

## 🏷️ The most important functions

- ![check](https://img.shields.io/badge/-Automatic%20structure%20validation-4caf50?style=flat-square&logo=checkmarx&logoColor=white)
- ![check](https://img.shields.io/badge/-Checking%20compatibility%20number%20offiles-2196f3?style=flat-square&logo=files&logoColor=white)
- ![check](https://img.shields.io/badge/-Verification%20for%20data.yaml-ff9800?style=flat-square&logo=yaml&logoColor=white)
- ![check](https://img.shields.io/badge/-Legible%20errors%20raports-e91e63?style=flat-square&logo=markdown&logoColor=white)

---

## 👨‍💻 Authors

- Gabriel Wiśniewski

---

## 📄 License

Project on Apache License Version 2.0.
