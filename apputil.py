import numpy as np


# update/add code below ...

def ways(n: int):
    # returns the number of ways to make n cents with pennies and nickels
    if n < 0:
        return 0
    return n // 5 + 1




def lowest_score(names, scores):
    #returns JUST the name of the person with the lowest score
    min_index = np.argmin(scores)
    return names[min_index]



def sort_names(names, scores):
    # returns the names in the order their scores in descending order
    sorted_indices = np.argsort(scores) [::-1]  # for sorting in descending order
    return names[sorted_indices]