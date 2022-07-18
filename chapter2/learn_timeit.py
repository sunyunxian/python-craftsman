import timeit

spend_time = timeit.timeit(stmt='[i for i in range(100000)]', number=1000)
print(spend_time)

spend_time = timeit.timeit(stmt='(i for i in range(100000))', number=1000)
print(spend_time)
