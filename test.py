from yololint.structure_validator import StructureValidator
from yololint.annotation_checker import AnnotationChecker
import os 
dataset_path = os.path.join(os.path.dirname(__file__), 'dataset')

# checker = StructureValidator(dataset_path)
# res = checker.dataset_validation()
# print(res)
labels_path = os.path.join(dataset_path, 'labels')
checker = AnnotationChecker(labels_path, 3)
print(checker.annotation_checker())

