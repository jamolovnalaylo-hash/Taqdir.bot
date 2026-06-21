"""
Taqdir Matritsasi hisoblash moduli
Aziz Numerolog metodikasi asosida
"""


def reduce_to_arcana(n: int) -> int:
    if n == 0:
        return 22
    while n > 22:
        n = sum(int(d) for d in str(n))
    return n


def calculate_matrix(day: int, month: int, year: int) -> dict:
    A = reduce_to_arcana(day)
    B = reduce_to_arcana(month)
    year_sum = sum(int(d) for d in str(year))
    C = reduce_to_arcana(year_sum)
    D_raw = A + B + C
    D = reduce_to_arcana(D_raw)
    E_raw = A + B + C + D
    E = reduce_to_arcana(E_raw)
    O = reduce_to_arcana(A + E)
    J = reduce_to_arcana(A + E)
    M = reduce_to_arcana(D + E)
    N = reduce_to_arcana(M + D)
    P = reduce_to_arcana(B + E)
    Q = reduce_to_arcana(C + E)
    L = reduce_to_arcana(E + C)
    R = reduce_to_arcana(M + L)
    R1 = reduce_to_arcana(R + M)
    R2 = reduce_to_arcana(R + L)
    F = reduce_to_arcana(A + B)
    G = reduce_to_arcana(B + C)
    H = reduce_to_arcana(C + D)
    I = reduce_to_arcana(A + D)
    K = reduce_to_arcana(B + E)
    F2 = reduce_to_arcana(F + L)
    G2 = reduce_to_arcana(G + L)
    chakras = {
        "sahasrara": reduce_to_arcana(A + B),
        "ajna": reduce_to_arcana(O + P),
        "vishudha": reduce_to_arcana(J + Q),
        "anahata": reduce_to_arcana(D + E),
        "manipura": E,
        "muladhara": reduce_to_arcana(C + D),
        "svadhisthana": reduce_to_arcana(M + N),
    }
    return {
        "A": A, "B": B, "C": C, "D": D, "E": E,
        "O": O, "J": J, "M": M, "N": N,
        "P": P, "Q": Q, "L": L,
        "R": R, "R1": R1, "R2": R2,
        "F": F, "G": G, "H": H, "I": I,
        "K": K, "F2": F2, "G2": G2,
        "chakras": chakras,
        "raw": {"day": day, "month": month, "year": year}
    }
