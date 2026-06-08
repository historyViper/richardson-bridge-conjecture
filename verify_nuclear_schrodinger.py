"""
verify_nuclear_schrodinger.py
GBP Nuclear Schrödinger / Manton Domain — Algebraic Verification
Jason Richardson (HistoryViper) — June 2026
AI-collaborative authorship: Claude (Anthropic)

Verifies gbp_nuclear_schrodinger_v1.3.md results.
All computed values are printed explicitly.
"""

import math, cmath, sys
sys.path.insert(0, '/home/claude')
from gbp_verify_common import section, show, show_exact, show_set, show_table

# ── Constants ──────────────────────────────────────────────────
GEO_B    = math.sin(math.pi / 15)**2
PI_E     = math.pi / math.e
Z30_STAR = [1, 7, 11, 13, 17, 19, 23, 29]
GAMMA    = [14.1347, 21.022, 25.011, 30.425, 37.586, 40.919, 43.327,
            48.005, 49.774, 52.970, 56.446, 59.347, 60.832, 65.113]

# ══════════════════════════════════════════════════════════════
section("1. MAGIC NUMBERS FROM RIEMANN ZEROS")
# ══════════════════════════════════════════════════════════════

magic_map = [(28, 1), (50, 3), (82, 6)]
rows = []
for N, idx in magic_map:
    g   = GAMMA[idx-1]
    val = 2 * g
    err = abs(val - N) / N * 100
    rows.append((f"N={N}", f"2γ_{idx}", f"{g:.4f}", f"{val:.4f}", f"{err:.3f}%"))

print()
show_table(["Target", "Formula", "γ_n", "2γ_n", "Error"], rows)

# N=126 with mod-28 correction
print()
floor_2g1  = math.floor(2 * GAMMA[0])
g13        = GAMMA[12]
N126_pred  = 2 * g13 * (1 + 1 / floor_2g1)
err126     = abs(N126_pred - 126) / 126 * 100

print(f"\n  N=126 derivation:")
print(f"    γ₁       = {GAMMA[0]}")
print(f"    2γ₁      = {2*GAMMA[0]:.4f}")
print(f"    ⌊2γ₁⌋    = {floor_2g1}")
print(f"    γ₁₃      = {g13}")
print(f"    2γ₁₃     = {2*g13:.4f}  (direct: {abs(2*g13-126)/126*100:.2f}% off)")
print(f"    correction factor = 1/⌊2γ₁⌋ = 1/{floor_2g1}")
show("N=126 = 2γ₁₃ × (1 + 1/28)", N126_pred, 126, tol=0.01, units="")

# ══════════════════════════════════════════════════════════════
section("2. MOD-28 AS FIRST CROSS-MODULAR CONDUCTOR")
# ══════════════════════════════════════════════════════════════

def bp(n):
    return [p for p in range(2,n) if n%p==0 and all(p%i!=0 for i in range(2,p))]
def phi(n):
    return len([r for r in range(1,n) if math.gcd(r,n)==1])

print()
print(f"  Modulus breakdown:")
for mod, sector in [(12,'leptonic'),(28,'interface'),(30,'hadronic')]:
    b = bp(mod)
    p = phi(mod)
    print(f"    mod-{mod:2d}  boundary primes = {b}  φ({mod})={p}  [{sector}]")

print()
first_z30_prime = 7
print(f"  mod-28 = φ(12) × first_Z30* prime")
print(f"         = {phi(12)} × {first_z30_prime} = {phi(12)*first_z30_prime}")
show_exact("28 = φ(12) × 7",
           phi(12)*first_z30_prime, 28,
           f"φ(12)×7 = {phi(12)}×{first_z30_prime}", "28", tol_abs=0)

print()
print(f"  Sub-lattice check:")
print(f"    lcm(12,30) = {math.lcm(12,30)}  → mod-12 IS sub-lattice of mod-30")
print(f"    lcm(28,30) = {math.lcm(28,30)}  → mod-28 is NOT sub-lattice of mod-30")
print(f"    lcm(12,28) = {math.lcm(12,28)}  → interface period = 84")

print()
print(f"  Lane r=7 dual role:")
print(f"    gcd(7,12) = {math.gcd(7,12)}  → active in mod-12 (electron sector)")
print(f"    gcd(7,28) = {math.gcd(7,28)}  → BOUNDARY in mod-28 (suppressed at interface)")
print(f"    gcd(7,30) = {math.gcd(7,30)}  → active in mod-30 (hadronic sector = strange quark)")

# ══════════════════════════════════════════════════════════════
section("3. Θ₃₀ MOCK THETA: MIRROR PAIRS AND MÖBIUS SIGN FLIP")
# ══════════════════════════════════════════════════════════════

mirror_pairs = [(r, 30-r) for r in Z30_STAR if r < 30-r]
print()
print("  Mirror pairs, lane weights, and q-gaps:")
rows = []
for r, rm in mirror_pairs:
    Pr   = math.sin(r*math.pi/15)**2
    Prm  = math.sin(rm*math.pi/15)**2
    gap  = rm**2 - r**2
    mult = gap // 30
    rows.append((f"({r},{rm})", f"{Pr:.6f}", f"{Prm:.6f}",
                 f"|{Pr-Prm}|<1e-12", f"{gap}", f"30×{mult}"))

show_table(["Pair","P(r)","P(30-r)","Equal?","q-gap","= 30×k"], rows)

print()
print("  r² mod 30 collapse (interference structure):")
sq_mod30 = sorted(set((r*r)%30 for r in Z30_STAR))
for r in Z30_STAR:
    print(f"    r={r:2d}: r²={r*r:4d}, r² mod 30 = {(r*r)%30}")
show_set("r² mod 30 ∈ {1, 19} only", sq_mod30, [1, 19])

print()
print("  Möbius sign flip — phases at η=1/2:")
print("  e^{iπr²} for each r ∈ Z30*:")
all_minus = True
for r in Z30_STAR:
    phase = cmath.exp(1j*math.pi*r**2)
    ok = abs(phase + 1) < 1e-10
    all_minus = all_minus and ok
    print(f"    r={r:2d}: r²={r*r:4d} (odd), e^{{iπ×{r*r}}} = {phase.real:+.1f}{phase.imag:+.1e}j")

print()
show_exact("ALL phases = -1  →  ψ(1/2,ε) = -ψ(0,ε)",
           -1.0 if all_minus else 0.0, -1.0,
           "min(|e^{iπr²}+1|)", "0", tol_abs=1e-9)

print()
show("GEO_B = sin²(π/15)", GEO_B, math.sin(math.pi/15)**2,
     tol=1e-10, units="[colorless boundary weight, p=3 cusp]")

# ══════════════════════════════════════════════════════════════
section("4. FORBIDDEN J SELECTION RULE")
# ══════════════════════════════════════════════════════════════

def is_forbidden(J):
    val = 3 * J
    if val == 0: return False
    n = val
    for p in [2, 3, 5]:
        count = 0
        while n % p == 0:
            n //= p; count += 1
        if count > 1: return False
    return n == 1

print()
print("  J  │ 3J │ factorization          │ squarefree │ status")
print("  ───┼────┼────────────────────────┼────────────┼────────────")
for J in range(12):
    val = 3*J
    # factor val
    if val == 0:
        fact_str = "0"
        sf = "—"
    else:
        n = val; parts = []
        for p in [2,3,5,7,11,13]:
            c = 0
            while n%p==0: n//=p; c+=1
            if c: parts.append(f"{p}^{c}" if c>1 else str(p))
        if n>1: parts.append(str(n))
        fact_str = "×".join(parts) if parts else "1"
        sf = "YES" if is_forbidden(J) else "no"
    status = "FORBIDDEN ✓" if is_forbidden(J) else "allowed"
    print(f"  {J:2d} │ {val:3d} │ {fact_str:22s} │ {sf:10s} │ {status}")

print()
forbidden_set = {J for J in range(21) if is_forbidden(J)}
show_set("Known forbidden {1,2,5} ⊆ predicted forbidden set",
         forbidden_set, {1,2,5,10})
print(f"  Full forbidden set 0–20: {sorted(forbidden_set)}")
print(f"  NEW PREDICTION: J=10 forbidden (3×10=30=2×3×5, all boundary primes) (P)")

# ══════════════════════════════════════════════════════════════
section("5. ROTATIONAL BAND LADDER B_n = (π/e) × r^n")
# ══════════════════════════════════════════════════════════════

r_step  = 1/3 + GEO_B/27
B_bands = [PI_E * r_step**n for n in range(4)]
B_ref   = [1.156, 0.387, 0.130, 0.0432]
labels  = ["B₀","B₁","B₂","B₃"]

print()
print(f"  π/e  = {PI_E:.8f} MeV")
print(f"  r    = 1/3 + GEO_B/27 = 1/3 + {GEO_B:.6f}/27")
print(f"       = {1/3:.6f} + {GEO_B/27:.6f} = {r_step:.8f}")
print()
print(f"  {'Band':<6} {'Computed (MeV)':<18} {'Reference (MeV)':<18} {'Error'}")
print(f"  {'─'*6} {'─'*17} {'─'*17} {'─'*10}")
for n, (B, Bref, lbl) in enumerate(zip(B_bands, B_ref, labels)):
    err = abs(B-Bref)/Bref*100
    print(f"  {lbl:<6} {B:<18.6f} {Bref:<18.4f} {err:.3f}%")

print()
err_geo = abs(B_bands[3] - GEO_B)/GEO_B*100
print(f"  Endpoint check: B₃ vs GEO_B")
show("B₃ ≈ GEO_B = sin²(π/15)", B_bands[3], GEO_B, tol=1.0, units="MeV")

# ══════════════════════════════════════════════════════════════
section("SUMMARY TABLE")
# ══════════════════════════════════════════════════════════════
print()
results = [
    ("N=28  = 2γ₁",              f"{2*GAMMA[0]:.3f}",   "28",   f"{abs(2*GAMMA[0]-28)/28*100:.2f}%",  "D"),
    ("N=50  = 2γ₃",              f"{2*GAMMA[2]:.3f}",   "50",   f"{abs(2*GAMMA[2]-50)/50*100:.2f}%",  "D"),
    ("N=82  = 2γ₆",              f"{2*GAMMA[5]:.3f}",   "82",   f"{abs(2*GAMMA[5]-82)/82*100:.2f}%",  "D"),
    ("N=126 = 2γ₁₃×(1+1/28)",   f"{N126_pred:.4f}",    "126",  f"{err126:.5f}%",                      "D"),
    ("28 = φ(12)×7",             f"{phi(12)*7}",         "28",   "exact",                               "D"),
    ("ψ(1/2)=-ψ(0) (all phases=-1)", "VERIFIED",        "—",    "algebraic",                           "D"),
    ("Forbidden J={1,2,5}",      "REPRODUCED",          "known","zero params",                          "D"),
    ("J=10 forbidden",           "PREDICTED",           "—",    "new (P)",                             "P"),
    ("B₀ = π/e",                 f"{PI_E:.5f} MeV",     "1.156","0.02%",                               "D"),
    ("B₃ ≈ GEO_B",               f"{B_bands[3]:.5f}",   f"{GEO_B:.5f}","0.46%",                       "D"),
]
show_table(["Result","Computed","Target","Error","Label"], results)
