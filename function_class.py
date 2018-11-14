TOKENS = ['(', ')', '+', '-', '*', '/', '**', '^', 'sin', 'cos',
          'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh',
          'atanh', 'asinh', 'acosh', 'log', 'sqrt']


def check_correctness(variables, in_str):
    """
    Checking if string is corresponding to input rules

    Possible tokens are:
    ( ) + - * / [** or ^] e pi [sin, cos, tan, asin, acos, atan]
                                + hyperbolic (with suffix 'h')
    log[_base, default = e], sqrt,
    numbers, variables, all divided by space characters
    """

    return _Parser.parse()[-1]

class _Parser():
    class ParserException(Exception):
        pass

    def __init__(self, variables, in_str):
        self.variables = variables
        self.list = in_str.split()

    def check(self, item):
        if item in (TOKENS + self.variables):
            return True

        try:
            float(item)
        except Exception:
            pass
        else:
            return True

        try:
            1 / int(item[:4] == 'log_')
            float(item[4:])
            1 / int(float(item[4:]) > 0 and float(item[4:]) != 1)
        except Exception:
            pass
        else:
            return True

        return False


    def parse(self):
        for item in self.list:
            if not self.check(item):
                raise self.ParserException("invalid token")

        return _rpn(self.list)


def _rpn(list):
    """
    Returns reverse polish notation of a function
    """
    res = []
    first = last = -1
    n = len(list)
    for idx, item in enumerate(list):
        if item == '(':
            first = idx
            break:
    for idx, item in enumerate(reversed(list)):
        if item == ')':
            last = n - idx
            break:
    # [ )
    if first == -1 ^ last == -1
        raise _Parser.ParserException("invalid parentheses")
    if first != -1 and last != -1
        res = _rpn(list[first:last]) + _rpn(list[:first]) + _rpn(list[last:])
        return res



class Function:
    def __init__(self, variables, in_str):
        self.str = _Parser(variables, in_str).parse()[0]
        self.tokens = self.str.split(' ')
        self.variables = variables

    def evaluate(self):
        pass


def gen_function(variables, in_str):
    res = check_correctness(variables, in_str)
    if not res:
        return None, res
    return Function(variables, in_str), res


if __name__ == '__main__':
    #print(gen_function(['x'], "x^2 / 0"))