import time
import math

testrange = [10, 100, 1000, 10000]

complexity_functions = [
            ["Konstant", lambda n: 1],
            ["Logarithmisch", lambda n: math.log(n)],
            ["log^2(n)", lambda n: math.log(n) * math.log(n)],
            ["Linear", lambda n: n],
            ["n*log(n)", lambda n: n * math.log(n)],
            ["n*log2(n)", lambda n: n * math.log2(n)],
            ["Quadratisch", lambda n: math.pow(n, 2)],
            ["Kubisch", lambda n: math.pow(n, 3)],
            #["Exponentiell", lambda n: math.pow(2, n)] # dont use it
        ]


def test(function):

    def wrapped(*args, **kw):

        results = []
        cf_results = list(map(lambda m: [m[0], []], complexity_functions))

        print("Test complexity of {}".format(function.__name__))

        start = time.time()
        for n in testrange:
            results.append(function(n, *args, **kw))
        end = time.time()

        for n in testrange:
            for i, c in enumerate(complexity_functions):
                cf_results[i][1].append(c[1](n))

        print("Duration: {} ms".format((end - start) * 1000))
        print("-- Results -----------------------------")
        print("Testrange {}".format(testrange))
        print("Function", results)
        for i, r in enumerate(cf_results):
            f = list(map(lambda x1, x2: x1/x2, r[1], results)) # divide through results
            f = list(map(lambda x: round(x/f[0], 3), f)) # divide all elements through first element
            print(r[0], round(sum(f)/len(f)-1, 2)*100, "%")
        print("----------------------------------------")

    return wrapped
