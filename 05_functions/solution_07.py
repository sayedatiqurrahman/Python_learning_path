
def sum_of_star_args(*args):
#    this *args will accept tuple  data type
    ms = 0
    for arg in args:
         if not isinstance(arg, (int, float)):
            raise ValueError("All arguments must be numbers.")
         ms+=arg

    return {"direct_sum_func": sum(args), 
            "manual_sum_func": ms}


print(sum_of_star_args(1, 2, 3)) # Output: 6