def is_obama(num):
    """Takes a number and checks if it is a year Obama won."""

    try:
        return (num == 2008 or num == 2012)
    except:
        print("Please enter a number")