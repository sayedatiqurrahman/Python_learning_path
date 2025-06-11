def kwargs_print(**kwargs):
   
    """
    This function accepts keyword arguments and prints them.
    It also returns a dictionary of the keyword arguments.
    """
    if not kwargs:
        raise ValueError("No keyword arguments provided.")
    

    for key, value in kwargs.items():
         
            print(f"{key}: {value}")

    return kwargs



print(kwargs_print(name="Alice", age=30, city="New York"))