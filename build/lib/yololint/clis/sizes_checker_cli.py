import argparse
from yololint.sizes_checker import SizesChecker

def main():
    parser = argparse.ArgumentParser(description="YOLO Dataset Sizes Checker CLI")
    parser.add_argument("width", type=int, help="Width of the images")
    parser.add_argument("height", type=int, help="Height of the images")
    parser.add_argument("dataset_path", help="Path to your dataset")
    args = parser.parse_args()
    
    checker = SizesChecker(args.width, args.height)
    result = checker.check_sizes(args.dataset_path)
    print(result)

if __name__ == "__main__":
    main()