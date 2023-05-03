import pytest
from main import active_elements_search


@pytest.mark.parametrize('path_to_file, active_elements_quantity',
                         [('test/tests_src/poe_test.jpg', 17)])
def test_active_elements_search_12x12_field(path_to_file, active_elements_quantity):
    assert active_elements_search(path_to_file) == active_elements_quantity
