from linq import Query
import statistics as stats

data = [(0, 0), (1, 1), (1, 2), (2, 1), (8, 0), (7, 2), (6, 1), (0, 1)]
other_data = [1, 2, 7, 0, 11, 11, 11, 11, 11, 11, 11, 55, 47]
q = Query(other_data).groupby(lambda x: x)
for k,v in q:
    print(k ,v)