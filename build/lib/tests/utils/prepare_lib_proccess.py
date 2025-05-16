from yololint.structure_validator import StructureValidator
from yololint.annotation_checker import AnnotationChecker

def prepare_lib_proccess(dataset_path, classes_count=0, target="structure"):
    checker = StructureValidator(dataset_path) if target == "structure" else AnnotationChecker(dataset_path, classes_count)
    result = checker.dataset_validation() if target == "structure" else checker.annotation_checker()
    return result
