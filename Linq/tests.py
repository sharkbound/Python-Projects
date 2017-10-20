from Linq import Query
import statistics as stats

data = [1, 2, 7, 0, 11, 60, 47]
other_data = [1, 2, 7, 0, 11, 55, 47]
q = Query(data).similar(other_data)
print(q)