from typing import Iterable


def _coerce_value(value) -> float:
    """
    Convert the input value to a float or integer, returning 0 for invalid inputs.

    The function returns an int if the input does not contain a decimal point,
    otherwise it returns a float.

    Args:
        value: The input value to convert (str, int, or float).

    Returns:
        int or float: The converted numeric value, or 0 if conversion fails.
    """
    try:
        if "." in value: 
            return float(value)
        else: 
            return int(value)
    except (TypeError, ValueError):
        return 0


def filter_ok(records: Iterable[dict], *, threshold: float = 0) -> list[dict]:
    """Return records with status=="ok" and value >= threshold.

    - Case-insensitive status handling, tolerates {"STATUS": ...} as well.
    - Ignores malformed records gracefully without side effects.

    Args:
        records: Iterable of dictionaries representing the data to filter
        threshold: Threshold used to impose a minimum value on the data
    """
    out: list[dict] = []
    for r in records:
        if not isinstance(r, dict):
            continue
        status = r.get("status", r.get("STATUS", "")).lower()
        if status == "ok":
            val = r.get("value", 0)
            if isinstance(val, str): 
                val = _coerce_value(val)
            if val >= threshold:
                out.append({"status": "ok", "value": val})
    return out


def compute(items):
    """
    Compute summary statistics of the given data.

    Computes:
        - count: number of records
        - sum: sum of the 'value' fields
        - avg: average of the 'value' fields

    Args:
        items: List of dictionaries representing the records to summarize. 
               Each dictionary should have a 'value' key.

    Returns:
        dict: Dictionary containing count, sum, and average of the values.
    """
    acc= []
    for it in items:
        acc.append(it.get("value",0))
    s = sum(acc)  
    avg = (s / len(acc)) if acc else 0
    return {"count":len(items),"sum":s,"avg":avg}