from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yololint",
    version="1.0.0",
    description="YOLO Dataset Debugger (yololint) is a tool for automatic validation and diagnostics of YOLO-format datasets. It helps you quickly detect common errors, inconsistencies, and missing files in your dataset structure and annotations before you start model training. With clear reports and easy usage, you save time and ensure your dataset is ready for deep learning projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
      
        "Source Code & Docs" :"https://github.com/Gabrli/YoloLint",
    },
    keywords="yolo, dataset, validation, lint, checker, annotation, computer vision, deep learning, machine learning, data quality, object detection, python, automation, data science, ai, neural networks, image processing, data preparation, error detection, data integrity",
    packages=find_packages(),
    author="Gabriel Wiśniewski",
    author_email="gabrys.wisniewski@op.pl",
    classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Topic :: Software Development :: Libraries",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache License Version 2.0",
    "Operating System :: OS Independent",
    ],
    install_requires=[
     "pyyaml",
    ],
    entry_points={
        "console_scripts":[
            "yololint-structure-v = yololint.clis.structure_validator_cli:main",
            "yololint-annotation-v = yololint.clis.annotation_checker:main",     
        ]
    },
)