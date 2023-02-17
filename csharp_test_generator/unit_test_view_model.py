from typing import List

# all of the data needed to populate test template
class UnitTestViewModel:
    def __init__(self, 
        test_class: str, 
        sut_class: str,
        namespace: str,
        dependency_declarations: List[str],
        dependency_initialization_lines: List[str],
        sut_initialization_lines: List[str]):

        self.test_class = test_class
        self.sut_class = sut_class
        self.namespace = namespace
        self.dependency_declarations = dependency_declarations
        self.dependency_initialization_lines = dependency_initialization_lines
        self.sut_initialization_lines = sut_initialization_lines

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False

        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"test class: {self.test_class}, \
            sut class: {self.sut_class}, \
            dependency_declarations: {self.dependency_declarations} \
            dependency_initialization_lines: {self.dependency_initialization_lines}, \
            sut_initialization_lines: {self.sut_initialization_lines}\
            "
