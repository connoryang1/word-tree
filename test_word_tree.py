import pytest
from word_tree import create_tree


@pytest.mark.parametrize("input,output", [("asdf", "((((f)d)s)a);\n")])
def test_create_tree(input: str, output: str) -> None:
    assert create_tree([input]).as_string("newick") == output
