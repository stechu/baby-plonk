from py_ecc.optimized_bls12_381 import G1, G2, curve_order, multiply
import secrets


def setup(N):
    """
    set up plonk circuits up to N gates
    """    
    s = secrets.randbelow(curve_order) # toxic waste
    acc = G1
    base_1 = []
    for i in range(N+3):
        base_1.append(acc)
        acc = multiply(acc, s)
    assert(len(base_1), N+3)
    return (base_1, [G2, multiply(G2, s)])

if __name__ == "__main__":
    print(setup(4))