from math import sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, \
                 atanh, asinh, acosh, log, sqrt, pi, e

TOKENS = ['(', ')', '+', '-', '*', '/', '**', '^', 'e', 'pi', 'sin', 'cos',
          'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh',
          'atanh', 'asinh', 'acosh', 'log', 'sqrt', 'ln']

PRIOR = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '**': 3,
    '^': 3
}

FUNCS = TOKENS[10:]
OPS = TOKENS[2:8]

class _Parser():
    """
    Checking if string is corresponding to input rules and returning RPN of the string

    Possible tokens are:
    ( ) + - * / [** or ^] e pi [sin, cos, tan, asin, acos, atan]
                                + hyperbolic (with suffix 'h')
    log[_base, default = e], sqrt,
    numbers, variables, all divided by space characters
    """
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


class _OP:
    @staticmethod
    def add(b, a):
        return a + b

    @staticmethod
    def sub(b, a):
        return a - b

    @staticmethod
    def mult(b, a):
        return a * b

    @staticmethod
    def div(b, a):
        return a / b

    @staticmethod
    def pow(b, a):
        return a ** b

    @staticmethod
    def uadd(a):
        return a

    @staticmethod
    def usub(a):
        return -a

    @staticmethod
    def log(a):
        return log(a)

    @staticmethod
    def log_(b, a):
        return log(b, a)

    @staticmethod
    def sqrt(a):
        return sqrt(a)

    @staticmethod
    def sin(a):
        return sin(a)

    @staticmethod
    def cos(a):
        return cos(a)

    @staticmethod
    def tan(a):
        return tan(a)

    @staticmethod
    def asin(a):
        return asin(a)

    @staticmethod
    def acos(a):
        return acos(a)

    @staticmethod
    def atan(a):
        return atan(a)
    
    @staticmethod
    def sinh(a):
        return sinh(a)

    @staticmethod
    def cosh(a):
        return cosh(a)

    @staticmethod
    def tanh(a):
        return tanh(a)

    @staticmethod
    def asinh(a):
        return asinh(a)

    @staticmethod
    def acosh(a):
        return acosh(a)

    @staticmethod
    def atanh(a):
        return atanh(a)


B_OP = {  # binary operator
    '+': _OP.add,
    '-': _OP.sub,
    '*': _OP.mult,
    '/': _OP.div,
    '**': _OP.pow,
    '^': _OP.pow,
    'log_': _OP.log_
}

U_OP = {  # unary operator
    'u+': _OP.uadd,
    'u-': _OP.usub,
    'log': _OP.log,
    'ln': _OP.log,
    'sqrt': _OP.sqrt,
    'sin': _OP.sin,
    'cos': _OP.cos,
    'tan': _OP.tan,
    'asin': _OP.asin,
    'acos': _OP.acos,
    'atan': _OP.atan,
    'sinh': _OP.sinh,
    'cosh': _OP.cosh,
    'tanh': _OP.tanh,
    'asinh': _OP.asinh,
    'acosh': _OP.acosh,
    'atanh': _OP.atanh,
}

CONSTS = {
    'e': e,
    'pi': pi
}

def _rpn(list):
    """
    Returns reverse polish notation of a function
    """
    res = []
    stack = []

    def is_func(func):
        return func in FUNCS or func[:4] == 'log_'

    for idx, item in enumerate(list):
        if item in OPS[:2] and (not idx or list[idx - 1] in TOKENS[:8] + FUNCS):
            stack.append("u" + item)  #unary
        elif is_func(item) or item == '(':
            stack.append(item)
        elif item == ')':
            while len(stack) and stack[-1] != '(':
                res.append(stack[-1])
                stack.pop()
            if not len(stack):
                raise _Parser.ParserException("invalid parentheses")
            stack.pop()
        elif item in OPS:
            while len(stack) and (is_func(stack[-1]) or (item in OPS[:4]) and PRIOR[stack[-1]] >= PRIOR[item]):
                res.append(stack[-1])
                stack.pop()
            stack.append(item)
        else:
            res.append(item)
    for item in reversed(stack):
        if item in TOKENS[:2]:
            raise _Parser.ParserException("invalid parentheses")
        res.append(item)
    stack.clear()
    return res


class Function:
    def __init__(self, variables, in_str):
        self.rpn = _Parser(variables, in_str).parse()
        self.variables = variables

    def evaluate(self, **kwargs):
        U_OPS = ['u+', 'u-'] + FUNCS
        stack = []

        for item in self.rpn:
            if item in OPS:
                stack.append(B_OP[item](stack.pop(), stack.pop()))
            elif item in U_OPS:
                stack.append(U_OP[item](stack.pop()))
            elif item in kwargs:
                stack.append(kwargs[item])
            elif item[:4] == 'log_':
                stack.append(B_OP[item[:4]](stack.pop(), float(item[4:])))
            elif item in CONSTS:
                stack.append(CONSTS[item])
            else:
                stack.append(float(item))

        if len(stack) != 1:
            raise _Parser.ParserException("something invalid, check expression again")

        return stack[0]


def gen_function(variables, in_str):
    try:
        res = Function(variables, in_str)
    except Exception:
        return None, False
    return res, True


if __name__ == '__main__':
    print(_rpn(['a', '+', 'b', '*', '2']))
    print(_rpn(['a', '^', 'b', '**', 'c']))
    print(_rpn(['a', '+', 'b', '*', 'c', '^', 'd']))
    print(_rpn(['a', '^', 'b', '*', 'c', '+', 'd']))
    func, res = gen_function(['x'], "x ^ 2 / 10")
    print(func, res)
    print(func.evaluate(x=3))

    func, res = gen_function(['x', 'y'], "x ^ 3 + y ^ 2 / 10")
    print(func, res)
    print(func.evaluate(x=3, y=5))

    func, res = gen_function([], "e ^ 2 / e")
    print(func, res)
    print(func.evaluate())

    func, res = gen_function(['x'], "sin ( x )")
    print(func, res)
    print(func.evaluate(x=pi/6))

    func, res = gen_function(['x'], "ln ( x )")
    print(func, res)
    print(func.evaluate(x=e))

    func, res = gen_function(['x'], "log_2 ( x )")
    print(func, res)
    print(func.evaluate(x=8))

    func, res = gen_function(['x'], "sin ( e ^ x ) * ln 66")
    print(func, res)
    print(func.evaluate(x=9))
