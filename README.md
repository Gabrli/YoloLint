# YOLO Dataset Debugger - (YoloLint)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/Apache-License-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![YOLO](https://img.shields.io/badge/YOLO-Dataset-yellow)
![Linting](https://img.shields.io/badge/Linting-PEP8-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-success)

---

## 🚀 About

**YoloLint** is a tool for automatic validation of dataset structure, annotation files, and image sizes in YOLO projects. It helps you catch typical errors in directory structure, YAML files, annotation files, and now also ensures all your images have the correct size before you start model training.

---

## 📦 Directory Structure

```
.
├── yololint/
│   ├── clis/
│   │   ├── structure_validator_cli.py
│   │   ├── annotation_checker_cli.py
│   │   └── sizes_checker_cli.py
│   ├── structure_validator.py
│   ├── annotation_checker.py
│   ├── sizes_checker.py
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

## 🖥️ Available Console Scripts

After installing the package, you can use the following commands in your terminal:

### Structure validation

```sh
yololint-structure-v <path_to_your_dataset>
```

### Annotation validation

```sh
yololint-annotation-v <path_to_labels_folder> <number_of_classes>
```

### Image size validation and rescaling

```sh
yololint-sizes-v <path_to_your_dataset> <width> <height>
```

---

## 📚 Documentation – How to Use

### Validate Dataset Structure

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

### Validate and Rescale Image Sizes

```python
from yololint.sizes_checker import SizesChecker

sizeX = 640  # expected width
sizeY = 480  # expected height
dataset_path = "/path/to/your/dataset"

checker = SizesChecker(sizeX, sizeY)
checker.check_sizes(dataset_path)
```
- **Function:** `SizesChecker.check_sizes(path_to_dataset)`
- **Description:** Checks if all images in the dataset have the specified size. If an image has a different size, you will be prompted in the terminal to rescale it automatically.

---

## 📝 Example `data.yaml`

```yaml
names: ['class1', 'class2', 'class3']
nc: 3
```

---

## 👨‍💻 Author

- Gabriel Wiśniewski

---

## 📄 License

Project is licensed under the Apache License.
