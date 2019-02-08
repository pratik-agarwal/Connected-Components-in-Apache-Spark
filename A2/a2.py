'''// File: a2.py \
* Pratik \
* Agarwal \
* I AFFIRM THAT WHEN WORKING ON THIS ASSIGNMENT \
* I WILL FOLLOW UB STUDENT CODE OF CONDUCT, AND \
* I WILL NOT VIOLATE ACADEMIC INTEGRITY RULES '''

from pyspark import SparkConf, SparkContext
import sys


def lSplit(data):
    line = data.split(" ")
    v = [int(x) for x in line]
    yield (v[0], v[1])
    yield (v[1], v[0])


def largeStarMap(data):
    u = data[0]
    v = data[1]
    yield (u, v)
    yield (v, u)


def smallStarMap(data):
    u = data[0]
    v = data[1]
    if u >= v:
        yield (u, v)
    else:
        yield (v, u)


def largeStarReduce(data):
    u = data[0]
    v = data[1]
    t = list(v)
    t.insert(len(t), u)
    m = min(t)
    for x in t:
        if x > u:
            yield x, m


def smallStarReduce(data):
    u = data[0]
    v = data[1]
    t = list(v)
    t.insert(len(t), u)
    m = min(t)
    for x in t:
        if x != m & x < u:
            yield x, m


if __name__ == '__main__':
    conf = SparkConf().setAppName("RDDcreate")
    sc = SparkContext(conf=conf)[]
    rddSS = sc.textFile(sys.argv[1]).flatMap(lSplit).groupByKey().flatMap(largeStarReduce).distinct()
    convergence = 1
    while convergence != 0:
        tempc = 1
        while tempc != 0:
            rddLS = rddSS.flatMap(largeStarMap).groupByKey().flatMap(largeStarReduce).distinct()
            rddSS = rddLS.flatMap(largeStarMap).groupByKey().flatMap(largeStarReduce).distinct()
            tempc = (rddLS.subtract(rddSS).union(rddSS.subtract(rddLS))).count()
        rddSS = rddLS.flatMap(smallStarMap).groupByKey().flatMap(smallStarReduce).distinct()
        convergence = (rddLS.subtract(rddSS).union(rddSS.subtract(rddLS))).count()
    rddSS.map(lambda (a, b): "{0} {1}".format(a, b)).coalesce(1).saveAsTextFile("Output")
    sc.stop()