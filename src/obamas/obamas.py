def is_obama(num):
    """Takes a number and checks if it is a year Obama won.
    
        Parameters
    ----------
    is_obama :  int
        A year as a whole number

    Returns
    -------
    True or False

    Examples
    --------
    >>> from obamas import obamas
    >>> is_obama(2008)
    """

    try:
        return (num == 2008 or num == 2012)
    except:
        print("Please enter a number")