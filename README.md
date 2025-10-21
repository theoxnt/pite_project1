# pite_project1

This project read data from a JSON file, execute a filter on it and then compute some new data with it (average, sum, length). 

## Installation

Clone the project :<br>
with HTTPS : git clone https://github.com/theoxnt/pite_project1.git<br>
with SSH : git clone git@github.com:theoxnt/pite_project1.git<br>

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
optional arguments :<br>
    --file "path_for_the_file" # indicate the path for the data file<br>
    --all<br> 
    --thres # the filter will use this threshold to only keep values better than it<br>

## Project structure 

pite_project1<br>
|<br>
|-- src/pite_project1/<br>
|    |<br>
|   |-- __init__.py<br>
|   |-- cli.py # command line treatment<br>
|   |-- config.py # Data class for the config<br>
|   |-- core.py # Main function : Enter point of the code<br> 
|   |-- data_generator.py # generate data if we don't have it and save it in /mnt/data/sample_100.json<br>
|   |-- io_.py # function to read, load or write in a file<br> 
|   |-- usefullFunctions.py # functions used in the main function in core.py<br>
|<br>
|-- tests<br>
|   |-- conftest.py<br>
|   |-- test_cli.py<br>
|   |-- test_core.py<br>
|   |-- usefullFunctionsTests.py<br>
|-- LICENSE<br>
|-- setup.py<br>

## Output example 

This is an exemple of output :<br> 
WARNING:__main__:[Errno 2] No such file or directory: 'data\\sample.json' - Could not read file, using backup data<br>
INFO:__main__:[2025/10/21-16:46:07] ok_count=2 total_value=10 avg=5.00<br>

## Tests 

To run all the tests, execute : 
```bash
python -m pytest -v tests
```
To run the tests of a specific file, execute :<br>
For example to test the useFullFunctions file
```bash
python -m pytest -v tests/usefullFunctionsTest.py
```

## License
This project use the MIT License



