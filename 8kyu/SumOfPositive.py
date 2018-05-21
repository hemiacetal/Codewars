def positive_sum(arr):

    return reduce(lambda n,m: n+m, filter(lambda x: x > 0,arr), 0)