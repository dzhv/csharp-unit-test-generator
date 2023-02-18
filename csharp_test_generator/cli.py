# Client interface for the library

from csharp_test_generator import sut_parser, view_model_mapper, template_builder
import pathlib as path

def main():
    # TODO: parse arguments and get csharp_file

    sut_file_path = "C:\\temp\\klase.cs"

    current_path = path.Path(__file__).parent
    template_path = current_path.joinpath('resources').joinpath('unit_test_template.txt')

    details = sut_parser.parse_file(sut_file_path)
    view_model = view_model_mapper.map_sut_details(details)
    output = template_builder.build(template_path, view_model)

    print("OUTPUT:\n")
    print(output)



if __name__ == "__main__":
    main()

