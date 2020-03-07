import sys

def error(message):
    """
    Displays error message and ends the current script

    Parameters
    ----------
    message : str
        Error message to be displayed.

    Returns
    -------
    None.

    """
    print("ERROR: "+message)
    sys.exit()