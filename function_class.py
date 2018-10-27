def _rpn(in_str):
    """
    Returns reverse polish notation of a function
    """
    return in_str



def check_correctness(variables, in_str):
    """
    Checking if string is corresponding to input rules

    Possible tokens are:
    ( ) + - * / [** or ^] e pi [sin, cos, tan, asin, acos, atan]
                        + hyperbolic (with suffix 'h')
    log[_base, default = e], sqrt
    """

    return True


class Function:
    def __init__(self, variables, in_str):
        self.str = _rpn(in_str)
        self.tokens = self.str.split(' ')
        self.variables = variables


def gen_function(variables, in_str):
    res = check_correctness(variables, in_str)
    if not res:
        return None, res
    return Function(variables, in_str), res
