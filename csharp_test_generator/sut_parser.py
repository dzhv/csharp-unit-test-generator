from typing import List, Optional
from csharp_test_generator.sut_details import SutDetails, SutDependency
import re

# parses the SUT C# class file
def parse_file(file_path: str) -> SutDetails:
    with open(file_path) as f:
        lines = f.read()
        return _parse(lines)

# parses the SUT C# class text
def _parse(text: str) -> SutDetails:
    class_name = _get_class_name(text)
    return SutDetails(class_name, "", _get_dependencies(text, class_name))

def _get_class_name(text: str) -> str:
     classes = re.findall(rf'public\s+class\s+(\S+)\s', text)
     # TODO deal with multiple classes
     return classes[0] if classes else None

def _get_dependencies(text: str, class_name: str) -> List[SutDependency]:
    # looks for constructor lines
    # captures argument list such as:
    # ICrew crew, IFuel fuel, Options options, \n        bool isOperational
    argumentCollections = re.findall(rf"public\s+{class_name}\(([^\)]*)\)", text)    
    if not argumentCollections:
        return []
    
    # TODO deal with multiple constructors
    argumentText = argumentCollections[0]

    return _parse_argument_text(argumentText)

def _parse_argument_text(argumentText: str) -> List[SutDependency]:
    arguments = [_parse_single_argument(text) for text in argumentText.split(',')]
    return [x for x in arguments if x is not None]
    
def _parse_single_argument(input: str) -> Optional[SutDependency]:
    # split here splits by whitespace
    parts = input.strip().split()
    if len(parts) != 2:
        return None

    return SutDependency(parts[0], parts[1])
