import pathlib as path
from csharp_test_generator import sut_parser

def test_parse_reads_class_name():
    current_path = path.Path(__file__).parent
    test_cases_path = current_path.joinpath('test_cases')
    file_path  = test_cases_path.joinpath('Airplane.cs')    

    actual = sut_parser.parse_file(file_path)

    assert "Airplane" == actual.class_name