from typing import List
from csharp_test_generator.sut_details import SutDetails, SutDependency
from csharp_test_generator.unit_test_view_model import UnitTestViewModel

def map_sut_details(sut_details: SutDetails) -> UnitTestViewModel:
    return UnitTestViewModel(
        test_class_name(sut_details.class_name), 
        sut_details.class_name,
        sut_details.namespace,
        map_dependency_declarations(sut_details.dependencies), 
        map_dependency_initialization_lines(sut_details.dependencies),
        get_sut_initialization(sut_details))

def test_class_name(class_name: str) -> str:
    return f"{class_name}Tests"

def map_dependency_declarations(dependencies: List[SutDependency]) -> List[str]:
    return [get_mock_dependency_declaration(dep) for dep in dependencies if dep.is_mockable()]

def get_mock_dependency_declaration(dependency: SutDependency) -> str:
    return f"private {get_mock_type(dependency)} {get_instance_name(dependency)};"

def map_dependency_initialization_lines(dependencies: List[SutDependency]) -> List[str]:
    return [get_dependency_initialization(dep) for dep in dependencies]

def get_dependency_initialization(dependency: SutDependency) -> str:
    if (dependency.is_mockable()):
        return f"{get_instance_name(dependency)} = new {get_mock_type(dependency)}();"

    return f"var {dependency.instance_name} = ???;"

def get_mock_type(dependency: SutDependency) -> str:
    return f"Mock<{dependency.type_name}>"

def get_instance_name(dependency: SutDependency) -> str:
    if (dependency.is_mockable()):
        return f"_{dependency.instance_name}"

    return dependency.instance_name

def get_sut_initialization(details: SutDetails) -> List[str]:
    dependency_params = [get_instance_name(dep) for dep in details.dependencies]
    constructor_call = ', '.join(dependency_params)
    return [ f"_sut = new {details.class_name}({constructor_call});" ] 