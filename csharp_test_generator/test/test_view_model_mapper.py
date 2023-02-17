from csharp_test_generator import view_model_mapper as mapper
from csharp_test_generator.sut_details import SutDetails, SutDependency
from csharp_test_generator.unit_test_view_model import UnitTestViewModel
from csharp_test_generator.test.utils import assert_equal


class TestViewModelMapper:
    # @classmethod
    # def setup_class(cls):
    #     current_path = path.Path(__file__).parent
    #     test_cases_path = current_path.joinpath('test_cases')
    #     cls.file_path  = test_cases_path.joinpath('Airplane.cs')    

    def test_map_sut_details(self):
        details = SutDetails("Airplane", "namespace", [
            SutDependency("ICrew", "crew"),
            SutDependency("Options", "options"),
            SutDependency("bool", "isOperational")
        ])

        expected = UnitTestViewModel("AirplaneTests",
            "Airplane",
            "namespace",
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
        
        actual = mapper.map_sut_details(details)

        assert_equal(actual, expected)

        