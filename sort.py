import random
from test import sorted
list = [random.randint(0,100) for i in range(random.randint(5,20))]
print('initial list:',(list))
sorted(list)
print('Sorted list:',(list))
