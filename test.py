from yololint.structure_validator import StructureValidator
import os
dataset_path = os.path.join(os.path.dirname(__file__), 'dataset')
checker = StructureValidator(dataset_path)
result = checker.dataset_validation()
print(result)