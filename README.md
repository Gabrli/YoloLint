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

## 📚 Documentation – How to Use

### Validate Dataset Structure

To check the correctness of your YOLO dataset folder structure and `data.yaml` file:

```python
from yololint.structure_validator import StructureValidator

dataset_path = "/path/to/your/dataset"
checker = StructureValidator(dataset_path)
result = checker.dataset_validation()
print(result)
```
- **Function:** `StructureValidator.dataset_validation()`
- **Description:** Checks if the folder structure and `data.yaml` are correct, and if the number of classes and class names match.

---

### Validate YOLO Annotation Files

To check the correctness of YOLO `.txt` annotation files:

```python
from yololint.annotation_checker import AnnotationChecker

labels_path = "/path/to/your/dataset/labels"
classes_count = 3  # number of classes in your dataset
checker = AnnotationChecker(labels_path, classes_count)
result = checker.annotation_checker()
print(result)
```
- **Function:** `AnnotationChecker.annotation_checker()`
- **Description:** Checks if all `.txt` files have the correct format (5 values per line, valid class_id) and are not empty.

---

### Command Line Interface (CLI)

You can also use the CLI tools after installing the package:

- **Structure validation:**
  ```sh
  yololint-structure-v <path_to_your_dataset>
  ```

- **Annotation validation:**
  ```sh
  yololint-annotation-v <path_to_labels_folder> <number_of_classes>
  ```

---

**Each function returns a clear text report indicating any errors or confirming that your data is correct.**

---

## 📝 Example of `data.yaml`

```yaml
names: ['class1', 'class2', 'class3']
nc: 3
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
