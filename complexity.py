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

        print("Test complexity of {} ...\r\n".format(function.__name__))

        f_results = []
        cf_results = list(map(lambda x: [x[0], []], complexity_functions))

        for n in testrange:
            f_results.append(function(n, *args, **kw))

            for i, c in enumerate(complexity_functions):
                cf_results[i][1].append(c[1](n))

        np_f_results = np.array(f_results)
        np_cf_results = list(map(lambda x: [x[0], np.array(x[1])], cf_results))

        data = []
        data.append([function.__name__, 0])

        for i, c in enumerate(np_cf_results):
            f = (np_f_results / c[1]) / (np_f_results[0] / c[1][0])
            divergence = (1 - np.sum(f) / len(f)) * 100

            data.append([c[0], divergence])

        data = sorted(data, key=lambda x: x[1], reverse=True)

        table_data = [
            ["Function", "Divergence"]
        ] + list(map(lambda x: [x[0], "{:.2f} %".format(x[1])], data))

        result_table = AsciiTable(table_data, "Results")

        print(AsciiTable([testrange, f_results], " Testrange ").table, "\r\n")
        print(result_table.table)

    return wrapped
