from yololint.structure_validator import StructureValidator
import os 
dataset_path = os.path.join(os.path.dirname(__file__), 'dataset')
validator = StructureValidator(dataset_path)
res = validator.dataset_validation()
print(res)