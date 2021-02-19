#import numpy as np
from ks_utils import *
import random

def quicksort(array, inDesiredOrder):
    _quicksort(array, 0, len(array)-1, inDesiredOrder)

def _quicksort(array, start, stop, inDesiredOrder):
    if start < stop:
        pivotindex = partitionrand(array, start, stop, inDesiredOrder)
        _quicksort(array, start, pivotindex-1, inDesiredOrder)
        _quicksort(array, pivotindex+1, stop, inDesiredOrder)

def partitionrand(array, start, stop, inDesiredOrder):
    randpivot = random.randrange(start, stop)
    array[start], array[randpivot] = array[randpivot], array[start]
    return partition(array, start, stop, inDesiredOrder)

def partition(array, start, stop, inDesiredOrder):
    pivot = start
    i = start + 1

    for j in range(start + 1, stop + 1):
        if inDesiredOrder(array[j].value, array[pivot].value):
        #if array[j].value >= array[pivot].value:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[pivot], array[i-1] = array[i-1], array[pivot]
    pivot = i - 1
    return pivot

def solve_greedy(items, capacity):
    # Ordenar de mayor a menor
    quicksort(items, lambda x, y: x >= y)
    value = 0
    weight = 0
    taken = [0]*len(items)
    
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, taken