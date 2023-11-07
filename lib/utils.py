# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def get_bytecode_size(func):
    """
    Calculate the size of the bytecode of the given function, including nested functions.
    """
    size = len(func.__code__.co_code)  # Size of the outer function bytecode

    # Check for nested functions and add their sizes
    for const in func.__code__.co_consts:
        if isinstance(const, type(func.__code__)):
            size += len(const.co_code)

    return size

def print_bytecode_size(func):
    print(f"Bytecode size of {func.__name__}: %d" % get_bytecode_size(func))
