from datetime import datetime
from pite_project1.usefullFunctions import filter_ok, compute
from pite_project1.io_ import load_json, load_config
from pite_project1.config import Config
from pite_project1.cli import get_parser
import logging

def main(display = True):
    """
    Main function : 
    - Load the configuration
    - Read the JSON data 
    - Apply filters and compute results
    - Return a dictionary containing the results 

    Args: 
        display (bool): Whether to print the result to stdout

    Returns:
        dict: A dictionary containing th computed metrics
    """

    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    logger = logging.getLogger(__name__)
    config = load_config()
    parser = get_parser()
    args = parser.parse_args()

    # Load the data (from argument or default config)
    if args.file:
        try:
            pth = args.file
            config = Config(pth, config.encoding, config.threshold, config.mode)
            data = load_json(config.path, config.encoding)
        except ValueError as e:
            logger.warning(f"{e} - Could not load file from args, continuing with data…")
    else: 
        try: 
            data = load_json(config.path, config.encoding)
        except Exception as e: 
            data = [
                {"STATUS":"ok","value":"3"}, 
                {"STATUS":"bad","value": "x"}, 
                {"STATUS":"ok","value":7}
            ]
            logger.warning(f"{e} - Could not read file, using backup data")

    
    # Update the configuration based on CLI arguments
    if args.all:
        config = Config(config.path, config.encoding, config.threshold, "ALL")
    if args.thres:
        try:
            config = Config(config.path, config.encoding, int(args.thres), config.mode)
        except Exception as e:
            logger.warning(f"{e} - Invalid threshold value, keeping default: {config.threshold}")

    # Filter and compute the results
    records = filter_ok(data, threshold=config.threshold)
    res = compute(records) 

    stamp = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    # Display the computed metrics (optional)
    if display:
        logger.info(f"[{stamp}] ok_count={res['count']} total_value={res['sum']} avg={res['avg']:.2f}")

    # Return the computed results
    return {
        "timestamp": stamp,
        "count": res["count"],
        "sum": res["sum"],
        "avg": res["avg"]
    }

if __name__ == "__main__":
    main()