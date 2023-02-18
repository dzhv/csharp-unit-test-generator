from setuptools import setup, find_packages

setup(
    name='generate_test',
    version='0.1',
    author='Dziugas Vysniauskas',
    description='A package for generating C# unit test boilerplate given a C# SUT class',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'generate_test=csharp_test_generator.cli:main'
        ]
    }
)