from python_utils.iterable_utils import count_element, unique_elements


def test_iter_utils():

    elements = [2, 1, 3, 1, 2, 1]

    assert count_element(elements, 1) == 3, "Nope !"

    assert len(unique_elements(elements)) == 3
