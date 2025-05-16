from .utils.prepare_lib_proccess import prepare_lib_proccess
import os

def test_annotation_checker():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    dataset_path = os.path.join(base_dir, 'dataset/labels')
    result = prepare_lib_proccess(dataset_path, 3, "annotation")
    assert isinstance(result, str)
    assert f"Your Errors: " in result
