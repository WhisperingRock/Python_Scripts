#Connor Wilson
# Logic gates for practice

import unittest


def buffer(a):
    return bool(a)


def inverter(a):
    return not bool(a)


def and_gate(a, b):
    return bool(a) and bool(b)


def or_gate(a, b):
    return bool(a) or bool(b)


def nand_gate(a, b):
    return not (bool(a) and bool(b))


def nor_gate(a, b):
    return not(bool(a) or bool(b))


def xor_gate(a, b):
    a = bool(a)
    b = bool(b)
    nand_ab = nand_gate(a, b)
    left = nand_gate(nand_ab, b)
    right = nand_gate(nand_ab, a)
    return nand_gate(left, right)


def xnor_gate(a, b):
    return not xor_gate(a, b)