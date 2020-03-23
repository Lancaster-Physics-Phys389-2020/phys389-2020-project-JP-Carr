def error(message,_exit=True):
    """
    Displays error message and ends the current script

    Parameters
    ----------
    message : str
        Error message to be displayed.
    
    _error : bool
        Exit main script?

    Returns
    -------
    None.

    """
    print("_______________________________________")
    print("\033[31mERROR: "+message)
    if _exit==True:
        from sys import exit
        exit()