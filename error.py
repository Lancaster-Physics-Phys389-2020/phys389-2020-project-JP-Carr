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
    print("\033[33mERROR: "+message) #red text
    if _exit==True:
        print("\a")
        from sys import exit
        exit()
        
    else:
        print("\033[1;39;47m") #revert to default text style