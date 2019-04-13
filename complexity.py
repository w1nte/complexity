import math
import numpy as np
from terminaltables import AsciiTable


class _Functions:
    """
    List of all Functions that should be tested
    """
    class Function:
        def __init__(self, name, function, args, kwargs):
            self.name = name
            self.function = function
            self.args = args
            self.kwargs = kwargs

        def run(self, n):
            return self.function(n, *self.args, **self.kwargs)

    def __init__(self):
        self.index = 0
        self.list = []

    def push(self, name, function, *args, **kwargs):
        self.list.append(self.Function(name, function, args, kwargs))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        else:
            self.index += 1
            return self.list[self.index - 1]


class _Results:
    """
    List of the tested Results
    """
    class Result:
        def __init__(self, name, results):
            self.name = name
            self.results = results

        def divergence(self, base=None):
            results = self.results
            if base:
                results = (base.results / results) / (base.results[0] / results[0])

            divergence = (1 - np.sum(results) / len(results)) * 100
            return divergence

    def __init__(self):
        self.list = []

    def push(self, name, results):
        self.list.append(self.Result(name, results))

    def get(self, name):
        for r in self.list:
            if r.name == name:
                return r
        return None

    def sorted_by_divergence(self):
        sorted_results = sorted(self.list, key=lambda x: x.divergence())
        return sorted_results


def _test(Functions):

    r = _Results()

    for f in Functions:
        results = np.array([])
        for t in testrange:
            results = np.append(results, f.run(t))

        r.push(f.name, results)

    return r

        
to_test = _Functions()
to_test.push("Constant", lambda n: 1)
to_test.push("Logarithmic", lambda n: math.log(n))
to_test.push("log^2(n)", lambda n: math.log(n) * math.log(n))
to_test.push("Linear", lambda n: n)
to_test.push("n*log(n)", lambda n: n * math.log(n))
to_test.push("Quadratic", lambda n: math.pow(n, 2))
to_test.push("Cubic", lambda n: math.pow(n, 3))
to_test.push('sqrt', lambda n: math.sqrt(n))

# range array that describes which n will be tested
testrange = [10, 100, 1000]


def queue(function, *args, **kw):
    """
    Adds a function to the test queue.

    The first Argument of the function has to be the input size n
    and has to return the costs.

    To run the test, call complexity.test()
    """
    to_test.push(function.__name__, function, *args, **kw)


def test(base="Linear"):
    """
    Tests all inserted functions.

    To add a new one, call complexity.queue(function).
    """
    if callable(base):
        base = base.__name__

    print("Test complexity of functions compared to {} ...".format(base), "\n")
    r = _test(to_test)

    b = r.get(base)

    table_data = [
        ["Function", "Divergence"]
    ] + list(map(lambda x: [x.name, "{:.2f} %".format(x.divergence(b))], r.sorted_by_divergence()))

    print(AsciiTable([testrange, b.results], " Testrange & function ").table, "\n")

    print(AsciiTable(table_data, " Results ").table)