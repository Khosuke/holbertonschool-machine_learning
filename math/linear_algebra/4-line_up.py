#!/usr/bin/env python3
"""
This module implement one function add_arrays(arr1, arr2).
"""


def add_arrays(arr1, arr2):
    """
    Function that adds two arrays element-wise.
    Args:
        arr1: first array.
        arr2: second array.
    """
    if len(arr1) != len(arr2):
        return None
    return [(arr1[i]+arr2[i]) for i in range(len(arr1))]
