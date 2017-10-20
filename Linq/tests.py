from Linq import Query

data = [1, None, 2, None, 3, 4, 5, 6, 7, None, None, 0]
q = Query(data).filter_nones()
print(q)