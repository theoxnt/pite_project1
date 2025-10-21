# pite_project1

This project read data from a JSON file, execute a filter on it and then compute some new data with it (average, sum, length). 

## Installation

Clone the project : 
with HTTPS : git clone https://github.com/theoxnt/pite_project1.git
with SSH : git clone git@github.com:theoxnt/pite_project1.git

## Running the code 
Create a new virtual environment, activate it and install the dependencies 
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
run the code
```bash
python -m src.pite_project1.core 
```
optional arguments : 
    --file "path_for_the_file" # indicate the path for the data file
    --all 
    --thres # the filter will use this threshold to only keep values better than it

## Project structure 

pite_project1
|
|-- src/pite_project1/
|    |
|   |-- __init__.py
|   |-- cli.py # command line treatment
|   |-- config.py # Data class for the config
|   |-- core.py # Main function : Enter point of the code 
|   |-- data_generator.py # generate data if we don't have it and save it in /mnt/data/sample_100.json
|   |-- io_.py # function to read, load or write in a file 
|   |-- usefullFunctions.py # functions used in the main function in core.py
|
|-- tests
|   |-- conftest.py
|   |-- test_cli.py
|   |-- test_core.py
|   |-- usefullFunctionsTests.py
|-- LICENSE
|-- setup.py

## Output example 

This is an exemple of output : 
WARNING:__main__:[Errno 2] No such file or directory: 'data\\sample.json' - Could not read file, using backup data
INFO:__main__:[2025/10/21-16:46:07] ok_count=2 total_value=10 avg=5.00

## Tests 

To run all the tests, execute : 
```bash
python -m pytest -v tests
```
To run the tests of a specific file, execute :
For example to test the useFullFunctions file
```bash
python -m pytest -v tests/usefullFunctionsTest.py
```

## License
This project use the MIT License



