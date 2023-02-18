from typing import List
from csharp_test_generator.sut_details import SutDetails, SutDependency
from csharp_test_generator.unit_test_view_model import UnitTestViewModel

def map_sut_details(sut_details: SutDetails) -> UnitTestViewModel:
    return UnitTestViewModel(
        _test_class_name(sut_details.class_name), 
        sut_details.class_name,
        sut_details.namespace,
        _map_dependency_declarations(sut_details.dependencies), 
        _map_dependency_initialization_lines(sut_details.dependencies),
        _get_sut_initialization(sut_details))

def _test_class_name(class_name: str) -> str:
    return f"{class_name}Tests"

def _map_dependency_declarations(dependencies: List[SutDependency]) -> List[str]:
    return [_get_mock_dependency_declaration(dep) for dep in dependencies if dep.is_mockable()]

def _get_mock_dependency_declaration(dependency: SutDependency) -> str:
    return f"private {_get_mock_type(dependency)} {_get_instance_name(dependency)};"

def _map_dependency_initialization_lines(dependencies: List[SutDependency]) -> List[str]:
    return [_get_dependency_initialization(dep) for dep in dependencies]

def _get_dependency_initialization(dependency: SutDependency) -> str:
    if (dependency.is_mockable()):
        return f"{_get_instance_name(dependency)} = new {_get_mock_type(dependency)}();"

    return f"var {dependency.instance_name} = ???;"

def _get_mock_type(dependency: SutDependency) -> str:
    return f"Mock<{dependency.type_name}>"

def _get_instance_name(dependency: SutDependency) -> str:
    if (dependency.is_mockable()):
        return f"_{dependency.instance_name}"

    return dependency.instance_name

def _get_sut_initialization(details: SutDetails) -> List[str]:
    dependency_params = [_get_instance_name(dep) for dep in details.dependencies]
    constructor_call = ', '.join(dependency_params)
    return [ f"_sut = new {details.class_name}({constructor_call});" ] 