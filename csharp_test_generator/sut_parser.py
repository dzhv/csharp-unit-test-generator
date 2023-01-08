from csharp_test_generator.sut_details import SutDetails
import re

# parses the SUT C# class file into SutDetails
def parse_file(file_path: str) -> SutDetails:
    with open(file_path) as f:
        lines = f.read()
        return parse(lines)

# parses the SUT C# class text into SutDetails
def parse(text: str) -> SutDetails:
    return SutDetails(get_class_name(text))

def get_class_name(text: str) -> str:
     classes = re.findall(r'public\s+class\s+(\S+)\s', text)     
     # TODO deal with multiple classes
     return classes[0] if classes else None
    