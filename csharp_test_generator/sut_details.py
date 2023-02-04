from typing import List

class SutDependency:
    def __init__(self, type_name: str, instance_name: str):
        self.type_name = type_name
        self.instance_name = instance_name

    def is_mockable(self):
        return self.type_name.lower().startswith("I")

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False

        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"Type name: {self.type_name}, Instance name: {self.instance_name}"

# Holds information about the C# class for which we want to generate a test
class SutDetails:
    def __init__(self, class_name: str, namespace: str, dependencies: List[SutDependency]):
        self.class_name = class_name       
        self.dependencies = dependencies

    def test_class_name(self):
        return f"${self.class_name}Tests"
    