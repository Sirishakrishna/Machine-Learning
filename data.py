import numpy
from scipy import stats
"""
We can split the data types into three main categories:

    Numerical
    Categorical
    Ordinal

Numerical data are numbers, and can be split into two numerical categories:

    Discrete Data
    - numbers that are limited to integers. Example: The number of cars passing by.
    Continuous Data
    - numbers that are of infinite value. Example: The price of an item, or the size of an item

Categorical data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.

Ordinal data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.

By knowing the data type of your data source, you will be able to know what technique to use when analyzing them.

In Machine Learning (and in mathematics) there are often three values that interests us:

    Mean - The average value
    Median - The mid point value
    Mode - The most common value
    
"""
    
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] 
x = numpy.mean(speed)
print(x)
y=numpy.median(speed)
print(y)
z=stats.mode(speed)
print(z)
    
    
    
    

