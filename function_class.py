def RPN(in_str):
    """
    Returns reverse polish notation of a function
    """
    return in_str


def check_correctness(variables, in_str):
    """
    Checking if string is corresponding to input rules
    """
    return True


class Function:
    def __init__(self, variables, in_str):
        self.str = RPN(in_str)
        self.tokens = self.str.split(' ')
        self.variables = variables


def GenFunction(variables, in_str):
    res = check_correctness(variables, in_str)
    if not res:
        return None, res
    return Function(variables, in_str), res
