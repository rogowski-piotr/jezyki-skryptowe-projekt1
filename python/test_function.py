import pytest
from str_strip import function


@pytest.mark.parametrize('text', ['acbca', ''])
@pytest.mark.parametrize('excluded', ['ac', None])
def test_correctness(text, excluded):
    orginal_function_result = text.strip(excluded)
    custom_function_result = function(characters=text, exclude_characters=excluded)
    assert custom_function_result == orginal_function_result