# pite_project1

This project reads data from a JSON file, it applies a filter to it and then computes new data from it (average, sum, length). 

Detailed description : <br>
The JSON file represents a list of dictionaries. In each dictionary there are two keys. The first one is the status (ok, bad or error). The second one is the value (int, float or str). The filter function keeps only the value that are greater than a threshold. Then a function computes the average and the sum of all the values left and to determine how many values are left. 

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
Run the code
```bash
python -m src.pite_project1.core 
```
Optional arguments :<br>
    --file "path_for_the_file" # indicate the path for the data file<br>
    --all<br> 
    --thres # the filter will use this threshold to only keep values better than it<br>

If you want to generate values, execute : 
```bash
python src.pite_project1.data_generator
```
It creates a file of data at the path /mnt/data/sample_100.json <br>

## Project structure 

Project structure:

```text
pite_project1/
├── src/pite_project1/
│   ├── __init__.py
│   ├── cli.py               # command line treatment
│   ├── config.py            # Data class for the config
│   ├── core.py              # Main function: entry point
│   ├── data_generator.py    # generate data if we don't have it
│   ├── io_.py               # functions to read/write files
│   └── usefulFunctions.py   # helper functions for core.py
├── tests/
│   ├── conftest.py
│   ├── test_cli.py
│   ├── test_core.py
│   └── usefulFunctionsTests.py
├── LICENSE
└── setup.py
```



## Output example 

This is an example of output :<br> 
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
This project uses the MIT License

## How to use this project as a package 

In your code : 
To import the core and io_ modules :
```bash
from pite_project1 import * 
```

To import and use the core module:
```bash
from pite_project1 import core
...
core.main()
```
Or you can use a shortcut :
```bash
from pite_project1 import main
...
main()
```

To import and use the io_ module :
```bash
from pite_project1 import io_
...
io_.load_json(path)
io_.dump_json(path, records)
io_.load_config(path)
```


