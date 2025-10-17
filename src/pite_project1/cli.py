import argparse

def get_parser():
    """
    Build an return the CLI argument parser 

    Returns: 
        argparse.ArgumentParser: Configured parser for the project
    """
    parser = argparse.ArgumentParser(description="Command-line interface of the project")
    parser.add_argument('--file', help="Path to the input data file.")
    parser.add_argument('--all', action='store_true', help="Enable all-mode processing.")
    parser.add_argument('--thres', help="Threshold value used for filtering.")
    return parser