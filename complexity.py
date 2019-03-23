import math
import numpy as np
from terminaltables import AsciiTable

testrange = [10, 100, 1000, 10000]

complexity_functions = [
            ["Constant", lambda n: 1],
            ["Logarithmic", lambda n: math.log(n)],
            ["log^2(n)", lambda n: math.log(n) * math.log(n)],
            ["Linear", lambda n: n],
            ["n*log(n)", lambda n: n * math.log(n)],
            ["n*log2(n)", lambda n: n * math.log2(n)],
            ["Quadratic", lambda n: math.pow(n, 2)],
            ["Cubic", lambda n: math.pow(n, 3)],
            #["Exponentiell", lambda n: math.pow(2, n)] # dont use it
        ]


def test(function):

    def wrapped(*args, **kw):

        results = []
        cf_results = list(map(lambda x: [x[0], []], complexity_functions))

        print("Test complexity of {}\r\n".format(function.__name__))

        for n in testrange:
            results.append(function(n, *args, **kw))

            for i, c in enumerate(complexity_functions):
                cf_results[i][1].append(c[1](n))

        results = np.array(results)
        cf_results = list(map(lambda x: [x[0], np.array(x[1])], cf_results))

        table_data = [
            ["Function", "Divergence"]
        ]
        print(AsciiTable([testrange], "Testrange").table)

        for i, c in enumerate(cf_results):
            f = (results / c[1]) / (results[0] / c[1][0])
            divergence = (np.sum(f) / len(f) - 1) * 100

            table_data.append([c[0], "{:.2f} %".format(divergence)])

        result_table = AsciiTable(table_data, "Results")
        print(result_table.table)

    return wrapped
