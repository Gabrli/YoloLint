from .utils.prepare_lib_proccess import prepare_lib_proccess
import os
def test_structurte_validator():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    dataset_path = os.path.join(base_dir, 'dataset')
    result = prepare_lib_proccess(dataset_path)
    print(result)
    assert isinstance(result, str)
    assert "Your Errors: " in result