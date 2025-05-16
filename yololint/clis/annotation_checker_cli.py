import argparse
from yololint.annotation_checker import AnnotationChecker

def main():
    parser = argparse.ArgumentParser(description="YOLO Dataset debugger CLI")
    parser.add_argument("labels_path", help="Path to your folder with labels")
    parser.add_argument("classes_count", help="Number of classes")
    args = parser.parse_args()
    checker = AnnotationChecker(args.labels_path, args.classes_count)
    result = checker.annotation_checker()
    print(result)

if __name__ == "__main__":
    main()