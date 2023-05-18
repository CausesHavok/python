import timeit
import random

"""Function for calculating the score based on the darts distance from the center"""
def score(x, y):
    """Calcualtes the score of a dart throw
    
    :param x float: The x coordinate of the dart
    :param y float: The y coordinate of the dart
    :return int: The score
    Calcualtes the score of the dart throw bases on the coordinates of the dart throw.
    Rules are as follows
    
    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.

    The outer circle has a radius of 10 units.
    The middle circle a radius of 5 units
    The inner circle a radius of 1.
    All circles have the same center point defined by the coordinates (0, 0).
    """
    #There is really no need to do sqrt/pow/** in this simple case
    distance_sqaured = x**2+y**2

    if distance_sqaured > 100: #10**2
        return 0
    if distance_sqaured > 25: #5**2
        return 1
    if distance_sqaured > 1: #1**2
        return 5
    
    return 10
