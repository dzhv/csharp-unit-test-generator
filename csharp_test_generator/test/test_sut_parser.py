import pathlib as path
from csharp_test_generator import sut_parser
from csharp_test_generator.sut_details import SutDetails, SutDependency


class TestSutParser:
    @classmethod
    def setup_class(cls):
        current_path = path.Path(__file__).parent
        test_cases_path = current_path.joinpath('test_cases')
        cls.file_path  = test_cases_path.joinpath('Airplane.cs')    

    def test_parse_reads_class_name(self):
        actual = sut_parser.parse_file(self.file_path)

        assert "Airplane" == actual.class_name

    def test_parse_reads_dependencies(self):
        actual = sut_parser.parse_file(self.file_path)

        assert actual.dependencies == [
            SutDependency("ICrew", "crew"),
            SutDependency("IFuel", "fuel"),
            SutDependency("Options", "options"),
            SutDependency("bool", "isOperational"),
        ]

        