"""
RSA encryption is a form of public-key cryptography.
The strength of RSA encryption depends on the fact 
 that getting the right factors is really really hard.
"""


# TODO: use this function at tasks.py
def find_factors(modules):
    factors = []
    for i in range(2, modules):
        if modules % i == 0:
            factors.append(i)

    if len(factors) == 0:
        factors.extend([1, modules])

    return factors
