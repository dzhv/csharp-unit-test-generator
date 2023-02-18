from csharp_test_generator.unit_test_view_model import UnitTestViewModel
from typing import List

def build(template_path: str, view_model: UnitTestViewModel) -> str:
    with open(template_path) as f:
        lines = f.read()
        return _fill(lines, view_model)

def _fill(template: str, view_model: UnitTestViewModel) -> str:
    return template \
        .replace("$NAMESPACE$", view_model.namespace) \
        .replace("$TEST_CLASS$", view_model.test_class) \
        .replace("$SUT_CLASS$", view_model.sut_class) \
        .replace("$DEPENDENCY_DECLARATIONS$", _join_multiple(view_model.dependency_declarations)) \
        .replace("$DEPENDENCY_INITIALIZATION$", _join_multiple(view_model.dependency_initialization_lines)) \
        .replace("$SUT_INITIALIZATION$", _join_multiple(view_model.sut_initialization_lines))

def _join_multiple(lines: List[str]):
    return '\n'.join(lines)