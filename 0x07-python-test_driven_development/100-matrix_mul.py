#!/usr/bin/python3
"""
function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """The code"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")
    
    m = len(m_a)
    n = len(m_a[0])
    q = len(m_b)
    p = len(m_b[0])
    
    for ma in m_a:
        if type(ma) != list:
            raise TypeError("m_a must be a list of lists")
        if len(ma) != n:
            raise TypeError("each row of m_a must be of the same size")
            
    for mb in m_b:
        if type(mb) != list:
            raise TypeError("m_b must be a list of lists")
        if len(mb) != p:
            raise TypeError("each row of m_b must be of the same size")
    if n != q:
        raise ValueError("m_a and m_b can't be multiplied")
    
    m_c = [[0 for i in range(p)] for j in range(m)]
    for i in range(len(m_c)):
        for j in range(len(m_c[i])):
            s = 0 
            for k in range(n):
                if type(m_a[i][k]) not in (int, float):
                    raise TypeError("m_a should contain only integers or floats")
                if type(m_b[k][j]) not in (int, float):
                    raise TypeError("m_b should contain only integers or floats")
                s += m_a[i][k]*m_b[k][j]
                m_c[i][j] = s
    return m_c
