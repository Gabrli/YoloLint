import argparse
from yololint.structure_validator import StructureValidator

def main():
    parser = argparse.ArgumentParser(description="YOLO Dataset Debugger CLI")
    parser.add_argument("dataset_path", help="Path to your dataset")
    args = parser.parse_args()
    checker = StructureValidator(args.dataset_path)
    result = checker.dataset_validation()
    print(result)

if __name__ == "__main__":
    main()