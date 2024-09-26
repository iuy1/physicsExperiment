import math
from typing import Iterable
from statistics import mean
import sympy as sp
import pandas as pd


def calculate_a_uncertainty(x: Iterable[float]):
    '''计算 A 类不确定度'''
    length = len(x)
    average_x = mean(x)
    s = math.sqrt(sum((xi - average_x)**2 for xi in x) / (length - 1))
    return s


def union_uncertainty(ua: float, ub: float):
    return math.sqrt(ua**2 + ub**2)


def indirect_uncertainty(f):
    '''返回间接不确定度计算公式'''
    vars: set = f.free_symbols
    parts = [sp.diff(f, var) * sp.Symbol('u_' + var.name) for var in vars]
    return sp.sqrt(sum(p**2 for p in parts))


if __name__ == '__main__':
    # simple test
    a, b, c = sp.symbols('a b c')
    print(indirect_uncertainty(a * b + c))
