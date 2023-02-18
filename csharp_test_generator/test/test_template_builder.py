import pathlib as path
from csharp_test_generator import template_builder as builder
from csharp_test_generator.unit_test_view_model import UnitTestViewModel


class TestTempalteBuilder:
    @classmethod
    def setup_class(self):
        current_path = path.Path(__file__).parent
        test_cases_path = current_path.joinpath('test_cases')
        self.file_path = test_cases_path.joinpath('unit_test_template.txt')
        self.expected_file_path = test_cases_path.joinpath('expected.txt')

    def test_parse_reads_class_name(self):
        view_model = UnitTestViewModel("AirplaneTests", "Airplane", "My.Airplane.Project", 
            [
                "private Mock<ICrew> _crew;"                
            ],
            [
                "_crew = new Mock<ICrew>();",
                "var options = ???;",
                "var isOperational = ???;"
            ],
            [   
                "_sut = new Airplane(_crew, options, isOperational);"
            ])

        with open(self.expected_file_path) as f:
            expected = f.read()

        actual = builder.build(self.file_path, view_model)

        assert actual == expected

        