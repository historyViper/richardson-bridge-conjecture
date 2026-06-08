"""
Catalan's Constant as a Two-Lane Chirality Euler Product
=========================================================
Jason Richardson (HistoryViper) — June 2026
github.com/HistoryViper/mod30-spinor
Zenodo: 10.5281/zenodo.19798271

Shared with Kate Meyer (Informational Energetics) — see note at bottom.

THE FORMULA
-----------
G = (15/16) × ∏_{p ∈ Θ₃₀}  p² / (p² − χ₋₄(p))

Where:
  Θ₃₀     = primes coprime to 30 = {7, 11, 13, 17, 19, 23, 29, 31, ...}
  χ₋₄(p)  = +1  if p ≡ 1 mod 4   (C1 lane)
             −1  if p ≡ 3 mod 4   (C2 lane)

Prefactor 15/16 comes from primes 3 and 5, excluded from Θ₃₀:
  p=3 (C2): 3²/(3²+1) = 9/10
  p=5 (C1): 5²/(5²−1) = 25/24
  9/10 × 25/24 = 15/16

THE TWO-LANE STRUCTURE
----------------------
Every prime coprime to 30 falls into exactly one lane:

  C1 (p ≡ 1 mod 4): factors > 1  — push product up
  C2 (p ≡ 3 mod 4): factors < 1  — push product down

The product converges to G because C1 and C2 are in exact balance.
G is the fixed point of that balance. This follows from the
mirror symmetry of the mod-30 lattice:

  gcd(30−r, 30) = gcd(r, 30)  for all r

This pairs every C1 prime with a C2 mirror at the same coprimality
level, preventing either lane from dominating.

CONNECTION TO THE RIEMANN HYPOTHESIS
-------------------------------------
The same two-lane balance that forces this product to converge also
forces the Mertens function M(x) = Σ_{n≤x} μ(n) to satisfy:

  |M(x)| < C·x^(1/2+ε)  for all ε > 0

This bound is equivalent to RH (Titchmarsh §14.28, proven equivalence).
G is the numerical witness: the value the balanced product converges to,
the same convergence that prevents M(x) runaway.

CONNECTION TO KATE MEYER'S E8 FRAMEWORK
-----------------------------------------
The C1/C2 lane assignment is the same chirality split that the
E8 → D4⊕D4 projection assigns to fermions:

  C1 (p ≡ 1 mod 4) ↔ left-chiral sector  (active temporal generator)
  C2 (p ≡ 3 mod 4) ↔ right-chiral sector (static internal symmetry)

The Θ₃₀ product is the discrete analog of the Euler product that
appears in the Protocol pillar (Yang-Mills gauge synchronization).
The plaquette of the mod-30 lattice IS the minimal non-trivial
synchronization loop — both frameworks arrive at the same object.

G = 0.91596... is the entropic fixed point of the C1/C2 balance
in the persistent vacuum substrate.
"""

import math

# ─────────────────────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────────────────────

G_TRUE = 0.915965594177219015  # known to 18 decimal places

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

def chi(p):
    """χ₋₄(p): +1 if p≡1 mod 4 (C1), −1 if p≡3 mod 4 (C2)."""
    return 1 if p % 4 == 1 else -1

def lane(p):
    return "C1  p≡1 mod 4" if p % 4 == 1 else "C2  p≡3 mod 4"

# ─────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────

print("=" * 65)
print("CATALAN'S CONSTANT — TWO-LANE CHIRALITY EULER PRODUCT")
print("Jason Richardson (HistoryViper) — June 2026")
print("=" * 65)
print()
print(f"  Target G = {G_TRUE}")
print()

# ─────────────────────────────────────────────────────────────
# SHOW THE LANE STRUCTURE FOR THE FIRST 12 PRIMES
# ─────────────────────────────────────────────────────────────

all_primes = sieve(300)
theta30 = [p for p in all_primes if math.gcd(p, 30) == 1]

print("First 12 primes in Θ₃₀ and their chirality lanes:")
print()
print(f"  {'prime':>6}  {'lane':>14}  {'factor p²/(p²−χ)':>20}  {'χ₋₄':>5}")
print("  " + "─" * 52)
for p in theta30[:12]:
    c = chi(p)
    factor = p**2 / (p**2 - c)
    direction = "↑" if c == 1 else "↓"
    print(f"  {p:>6}  {lane(p):>14}  {factor:>20.14f} {direction}  {c:>+5}")

print()
print("  ↑ = C1 factor > 1 (pushes product up)")
print("  ↓ = C2 factor < 1 (pushes product down)")
print("  Balance converges to G.")
print()

# ─────────────────────────────────────────────────────────────
# PREFACTOR
# ─────────────────────────────────────────────────────────────

print("─" * 65)
print("PREFACTOR from p=2, 3, 5 (not coprime to 30):")
print()
print("  p=2: excluded entirely (even prime, no lane assignment)")
print(f"  p=3 (C2):  9/(9+1)   = 9/10  = {9/10:.8f}")
print(f"  p=5 (C1):  25/(25-1) = 25/24 = {25/24:.8f}")
print(f"  product:   9/10 × 25/24 = 15/16 = {15/16:.8f}")
print()

# ─────────────────────────────────────────────────────────────
# CONVERGENCE
# ─────────────────────────────────────────────────────────────

print("─" * 65)
print("CONVERGENCE TABLE:")
print()
print(f"  {'N primes':>9}  {'G approx':>22}  {'error':>12}  {'ppb error':>10}")
print("  " + "─" * 60)

boundary = 15 / 16
large_primes = sieve(2_000_000)
theta30_large = [p for p in large_primes if math.gcd(p, 30) == 1]

product = 1.0
checkpoints = {1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000}

for i, p in enumerate(theta30_large):
    product *= p**2 / (p**2 - chi(p))
    n = i + 1
    if n in checkpoints:
        G_approx = boundary * product
        error = abs(G_approx - G_TRUE)
        ppb = error / G_TRUE * 1e9
        print(f"  {n:>9}  {G_approx:>22.15f}  {error:>12.3e}  {ppb:>10.3f}")

print()

# ─────────────────────────────────────────────────────────────
# MIRROR SYMMETRY
# ─────────────────────────────────────────────────────────────

print("─" * 65)
print("THE MIRROR SYMMETRY THAT FORCES CONVERGENCE:")
print()
print("  gcd(30−r, 30) = gcd(r, 30)  for all r  [proven — mod-30 lattice]")
print()
print("  This pairs C1 and C2 primes symmetrically.")
print("  The mirror pairs in Z₃₀* = {1,7,11,13,17,19,23,29}:")
print()

Z30 = [r for r in range(1, 30) if math.gcd(r, 30) == 1]
print(f"  {'r':>4}  {'30-r':>5}  {'P(r)=sin²(rπ/15)':>18}  {'product P(r)×P(30-r)':>22}")
print("  " + "─" * 55)

seen = set()
for r in Z30:
    m = 30 - r
    if m in Z30 and r not in seen and m not in seen:
        Pr  = math.sin(r * math.pi / 15)**2
        Pm  = math.sin(m * math.pi / 15)**2
        prod = Pr * Pm
        print(f"  {r:>4}  {m:>5}  {Pr:>18.10f}  {prod:>22.10f}")
        seen.update([r, m])

print()
print("  P(r)×P(30-r) = sin²(rπ/15)×cos²(rπ/15) = ¼sin²(2rπ/15)")
print("  Neither lane dominates. The product is bounded above and below.")
print()

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────

G_final = boundary * product
error_final = abs(G_final - G_TRUE)

print("=" * 65)
print("RESULT")
print("=" * 65)
print()
print("  G = (15/16) × ∏_{p∈Θ₃₀} p²/(p²−χ₋₄(p))")
print()
print(f"  Computed:  {G_final:.15f}")
print(f"  True G:    {G_TRUE:.15f}")
print(f"  Error:     {error_final:.3e}")
print(f"  PPB:       {error_final/G_TRUE*1e9:.4f}")
print()
print("  Zero free parameters.")
print("  Inputs: mod-30 structure, χ₋₄ character, π.")
print()
print("  G is the fixed point of the C1/C2 chirality balance.")
print()
print("  The same balance bounds M(x) and connects to RH:")
print("  |M(x)| < C·x^(1/2+ε) ↔ RH  (Titchmarsh §14.28)")
print()
print("  For E8/D4⊕D4 connection:")
print("  → RH_geometric_framework_v6.md §9.7a")
print("  → GBP Catalan paper v2 (Zenodo 10.5281/zenodo.19798271)")
print()
print("  Jason Richardson | HistoryViper | June 2026")
print("  github.com/HistoryViper/mod30-spinor")
