import numpy as np
import math
import sympy as sym
from scipy import linalg
from sympy import *

def limits_func_vec(vec, var, val):
    limits = np.array([])
    for i in range(0, len(vec)):
        limits = np.append(limits, sym.limit(vec[i], var, val))
    return limits

def deriv_func_vec(vec, var, num_of_derivs = 1, solve = False, val = None):
    if (solve == False and val == None):
        derivs = np.array([])
        for i in range(0, len(vec)):
            derivs = np.append(derivs, sym.diff(vec[i], var, num_of_derivs))
        return derivs
    else:
        derivs = np.array([])
        for i in range(0, len(vec)):
            derivs = np.append(derivs, sym.diff(vec[i], var, num_of_derivs))
        for i in range(0, len(vec)):
            derivs[i] = derivs[i].subs(var, val)
        return derivs

def integrate_func_vec(vec, var = None, start = None, end = None):
    if (start == None and end == None and var == None):
        integrals = np.array([])
        for i in range(0, len(vec)):
            integrals = np.append(integrals, sym.integrate(vec[i]))
        return integrals
    else:
        integrals = np.array([])
        for i in range(0, len(vec)):
            integrals = np.append(integrals, sym.integrate(vec[i], (var, start, end)))
        return integrals
