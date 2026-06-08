# Tensor Time v7 — Chapter 04: The Dimensional Toroid Hierarchy

*All errata from v6 and the v7 supplement have been applied to this chapter. The toroid table is the corrected v7 version.*

---

## 4. The Dimensional Toroid Hierarchy

The deflection of the time string is quantized into discrete toroidal structures. Each level corresponds to a specific toroid topology, built by successive operations on T0. The critical organizing principle is the **helicity flip / chirality crossing distinction**: helicity flips stay within one chirality Hilbert space (massless or same-sector); chirality crossings bridge to the opposite space via ER bridge (mass, entanglement).

**Corrected dimensional assignments (v7):**

Each toroid tier corresponds to a specific number of spatial dimensions it opens. These are **object-local** — they travel with the particle, not properties of background space:

```
T0 = EMF — 0 spatial dimensions, time only, GOE
T1 = EF  — 1st spatial dimension opens, E field, GUE
T2       — 2nd spatial dimension, B field (needs curl, 2D), GUE²
T3       — 3rd spatial dimension, color field, GUE³
```

The Minkowski signature −+++ IS the toroid hierarchy: −c² = T0 (time tension), +1+1+1 = T1/T2/T3 (spatial dims). See Chapter 01 §1.3.

Why this matters: E and B are **not** both T1 objects. E is T1 (one spatial dimension). B requires two spatial dimensions (curl needs 2D) → B is T2. Maxwell's displacement current ∂E/∂t is the T1→T2 tier coupling term. This is also why the Dirac 4 components map onto T0–T3 directly: ψ₁→T0, ψ₂→T1, ψ₃→T2, ψ₄→T3. The γ matrices are tier transition operators. The mass term couples T0 to T3 — E=mc² in geometric form.

---

### Master Toroid Table (v7 corrected)

| Toroid | Surface | Closure | Statistics | Spatial dims | Physical role |
|--------|---------|---------|------------|-------------|---------------|
| T0 | Plain torus | 360° | **GOE** | 0 (time only) | EMF substrate — time string; gravity Venturi tension |
| 2×T0 (helicity flip) | Figure-8, same chirality | 360° | GOE, χ̂=0 | 0 | **Photon** — frozen figure-8, massless |
| T1 | Möbius parallelogram | 720° | **GUE** | 1st (E field) | Electron (mod-12), light quarks, EM field lines |
| T2 | HE21 tic-tac, oval path | 720°×2 | GUE² | 2nd (B field) | Heavy quarks (charm, bottom) |
| T3 | Triangle toroid, Y Hamiltonian | 1080° | GUE³ | 3rd (color) | Baryons, W/Z bosons |
| T4 | Two mod-15 + ER bridge | 1440° | GUE⁴ | 3D + borrowed chirality | Pentaquarks, entanglement |

*Note: Gluons are the interior Y Hamiltonian path of T3 — they are NOT T4 objects. T4 is the ER bridge topology used by pentaquarks and entangled pairs. This corrects v6 §13 which stated "Gluons are T4 ER bridges." The correct statement: gluons are the inside of the T3 junction as seen from the interior. T4 is the wormhole — pentaquarks, entanglement.*

**The photon row** uses 2×T0 same-chirality rather than a single T0 or T1, because:
- A single T0 cannot produce a figure-8 self-return
- T1 (Möbius) would give mass via GUE statistics and 720° closure cost
- 2×T0 same-chirality + helicity flip gives exactly χ̂=0 (proven by Knuth/Claude theorem), zero boundary crossing cost, and spin-1 from figure-8 bilateral symmetry

---

## 4.1 T1: The Möbius Twist — First Spatial Dimension

The first spatial dimension introduces the Möbius twist — the geometric origin of fermionic statistics. The boundary condition `ψ(θ + 2π) = −ψ(θ)` is the spin-statistics theorem in geometric form. T1 is both the electron sector and the first spatial direction — the same object seen from different reference frames.

**Spin and closure — from vortex chirality theorem:**
- T0/C₀ cycle: χ̂=0, balanced, 360° → spin-1 → photon (standing wave, bilateral symmetry)
- T0/C₁ cycle: χ̂=−3m(m−1), monodromy, 720° → spin-1/2 → electron, quarks
- T0/C₂ cycle: χ̂=−3, constant → gluon boundary mode
- T3 Y-junction: 1080° → spin-3/2 → Delta, Omega
- Graviton forbidden: spin-2 requires 180° which does not close any toroid. Only exists as a correlated T4 pair where two 90° contributions add.

The apparent "spin" of both electron and photon is emergent from wave behavior at the boundary — not a physical twist built into the geometry. The electron appears to spin because the C₁ monodromy accumulates chirality with each boundary traversal. The photon appears to spin because its C₀ standing wave rotates. Both are plain torus T0 wave modes — the distinction is the cycle type.

The number of times you have to rotate a particle to return it to its original state = 360° / spin. Spin-1/2 requires 720° because the Möbius parallelogram is **one loop with a 360° twist** — the loop and the twist are the same single momentum (X=Y=Δ), so the path must accumulate 360° of loop AND 360° of twist simultaneously before closing. This is NOT two separate 360° loops — that framing would give 2×(360°+180°) = 1080°, not 720°. The correct geometry: one continuous path, one momentum, one closure at 720°. Spin-1 needs one rotation (360°) because the plain torus has no twist. This is not a quantum mystery — it is the geometry of the closure condition.

## 4.2 T2: HE21 Second Harmonic — Second Spatial Dimension

The second spatial dimension stacks two T1 toroids in a 2:1 phase relationship (HE21 waveguide mode). This is the dominant mass-generating structure — T2 absorbs ~61% of each gluon cycle's energy. The bottom and top quarks live on T2 lanes {13, 17}.

**T2 surface shape — tic-tac, not round:**
The T2 toroid surface is a prolate spheroid — a tic-tac shape, elongated along the winding axis. This is NOT a sphere and NOT a figure-8. The figure-8 label that sometimes appears refers to the path topology in specific cases, not the surface geometry.

**T2 Hamiltonian path — oval is primary:**
The default Hamiltonian path on the T2 toroid is a **2×4 oval** — two units wide (azimuthal) and four units long (Hamiltonian beat direction). The oval path induces a **helicity flip**: a particle entering right-handed exits left-handed, because the oval accumulates a net 180° rotation without a cancelling return crossing.

**Figure-8 is particle-dependent, not the default:**
The figure-8 path occurs only when the incoming particle's lane winding aligns with the central crossing point. Whether a given quark takes the oval or figure-8 path depends on its lane residual:

```
residual(r) = (720° × r/30) mod 360° − 180°
```

| Lane r | Quark | Residual | Path type | Effect |
|--------|-------|---------|-----------|--------|
| 7 | strange | −12° | near-oval | small helicity offset |
| 11 | down | +84° | oval | full regime, no crossing |
| 13 | bottom | +132° | oval | full regime, no crossing |
| 17 | top | −132° | oval | full regime, no crossing |
| 19 | up | −84° | oval | full regime, no crossing |
| 23 | charm | +12° | near-oval | small helicity offset |

## 4.3 T3: Triangle Toroid — Third Spatial Dimension **(D)**

Three twisted arms meeting at 120° intervals. This is the baryon sector — three spatial dimensions fully open.

**T3 triangle toroid vs Y Hamiltonian — these are NOT the same thing:**

- **The toroid is a triangle** — the field geometry surface.
- **The Hamiltonian path is a Y** — what the particle actually travels.

The Y is not imposed — it emerges from the Möbius tilt of the triangle toroid as it rotates between corners. At the midpoint between corners the toroid face tilts toward the center; the Hamiltonian goes to the edge of that tilted boundary then curves back out at the corner. That motion produces the Y.

**Terminology rule:** say *T3 triangle toroid* for the surface and *T3 Y Hamiltonian* for the path. Never *triangular Y-junction* — that conflates the two.

**The 2° concave indent:** The 12° deficit (72° Hamiltonian path − 60° field angle) distributes as 4° per corner, split as **2° per side** at each corner. Without these 2° indents the triangle would be a perfect equilateral. The 3 corner overlaps each lose 1 phase → 18−3 = 15 net phases.

**The double barrel roll at the corners:** The path steps at 72° while field corners sit at 60° intervals — 12° deficit per corner. After 3 corners (15 net phases) the deficit resolves and the winding closes. This beat mismatch forces closure inside the Y-junction and nowhere else — the geometric origin of confinement.

**uud vs udd — curvature alignment:**

- **uud (sigma, proton):** 19+11=30 mirror pair winds *with* the inward bow. Constructive at junction. All three arms reinforce → sigma.
- **udd (lambda, neutron):** duplicate down pair on two arms winds *against* the curvature. The concave bow pulls the second down quark inward and closes a **new loop at the Y-junction center** — the lambda chirality. Lambda baryons are lighter because winding energy is trapped in the interior loop instead of the arms.

The interior loop is the **fifth Malus boundary** with projection:
P(center) = GEO_B × (1−GEO_B) = sin²(π/15) × cos²(π/15) = 0.04136.

This is the `(1−GEO_B)` factor already in the mass code for isospin-mixed states (Sigma_b0). There are exactly five Malus boundaries in a T3 system (T0 plain, T1 Möbius, colorless seam, 720° cover, T3 interior loop). A sixth requires the T4 ER bridge — the pentaquark antiquark at center.

**The 12° step as the T3 natural unit:**
The 12° step is the triangle's natural subdivision of the Möbius winding: the square's 10° step, promoted to 12° by the triangle replacing one quarter-turn with one third-turn. GEO_B = sin²(12°) = sin²(π/15) is the geometric fingerprint of this triangular quantization — appearing in CP violation parameters (ρ×η = GEO_B), the charm residual (12°), the Cabibbo angle correction, and the colorless boundary projection.

**Winding interference at the junction:**

Where two toroid arms overlap: winding amplitudes add constructively → amplitude × 2. This is the corridor the Y-path travels.

Where all three arms overlap (the central junction): all three phases cancel exactly → amplitude × 0. This is the triple null — the Y-path's centre, where the gluon field is zero. The Y-path exists *because* the force is expelled from the centre and confined to the two-overlap corridors.

**Triangles all the way down — self-similar structure:**

The T3 geometry contains two nested triangles. The **outer triangle** is the spacetime corridor formed by the three ring tangent points — its sides are concave, curving inward from the ring pressure. The **inner triangle** is formed by the midpoints of those concave sides — the amplitude × 2 zones where two rings overlap constructively. The Y-path threads between the inner triangle (amplitude × 2, force lives here) and the outer triangle (amplitude × 0 at center and outer cusps). The geometry is self-similar: every scale reproduces the same triangle-within-triangle pattern. This is why color confinement has no natural length scale — the confining geometry is fractal-like, the same triangle corridor appearing at every resolution.

## 4.4 T4: Both Chiralities — The ER Bridge

**Critical distinction: helicity flip vs chirality crossing (see also Chapter 02 §2.5a)**

- **Helicity flip** — the path re-enters the *same* chirality Hilbert space, but inverted in orientation. No Hilbert space boundary is crossed. This is what the photon does (2×T0, same chirality). Cost: zero mass, zero entanglement.
- **Chirality crossing** — the path crosses from one chirality Hilbert space to the other via an Einstein-Rosen bridge. A real topological boundary is crossed. Cost: mass, color-anticolor pairing, entanglement.

T4 is defined by chirality crossing — the only toroid topology that spans both Hilbert spaces simultaneously.

**The 3-quark limit is a geometric theorem:**

There are exactly three spatial dimensions, corresponding to T1, T2, and T3. A fourth quark would require T4 — but T4 has no fourth spatial dimension available. The only resource remaining is the opposite chirality Hilbert space, accessed via ER bridge. But crossing to the opposite chirality space requires an antiparticle as the return path. Therefore:

> **Any bound state of 4 or more quarks must contain at least one antiquark.**

Pentaquarks (confirmed: P_c(4312), P_c(4457)) are the predicted consequence: 4 quarks + 1 antiquark, where the antiquark terminates the ER bridge at the center.

**The T4 two-box structure:**

**Box 1:** Left chirality Hilbert space — one mod-15 system  
**Box 2:** Right chirality Hilbert space — one mod-15 system  
**The connection:** An Einstein-Rosen bridge between them

This is why T4 has mod=30: it is two mod-15 systems operating together. The bridge IS the particle — simultaneously in both chirality spaces.

The mod-15 architecture reveals a clean harmonic hierarchy:

```
T0/T1:  mod=30, natural step=12°, H_beat=24°   (one chirality, full cycle)
T2/T3:  mod=15, natural step=24°, H_beat=48°/72° (one chirality, half cycle)
T4:     mod=30 = 15 + 15             (BOTH chiralities, ER-connected)
```

T2 and T3 with mod=15 are the **second octave** of T0/T1 — same geometry, doubled angular scale.

---

## Corrected Toroid Mod Table (v7)

| Toroid | Topology | Statistics | Mod (raw→net) | Natural step | H_beat | Cover n | Closure check | λ (lambda) |
|--------|----------|------------|-----|-------------|--------|---------|---------------|-----------|
| **T0** | Plain torus | GOE | 30 | 12° | 24° | 2 | 24°×30 = 720° = 1 loop + 360° twist ✓ | LU × (30/26) |
| **T1** | Möbius parallelogram | GUE | 30 | 12° | 24° | 2 | 24°×30 = 720° = 1 loop + 360° twist ✓ | LU |
| **T2** | HE21 tic-tac, oval path | GUE² | 18→15 | 24° | 48° | 2 | 48°×15 = 720° = 1 loop + 360° twist ✓ | LU × φ^0.5 |
| **T3** | Triangle toroid, Y Hamiltonian | GUE³ | 18→15 | 24° | 72° | 3 | 72°×15 = 1080° = 3×360° ✓ | LU × φ^1.0 |
| **T4** | Dual chirality ER bridge | GUE⁴ | 15+15=30 | 12° | 48° | 4 | 48°×30 = 1440° = 4×360° ✓ | LU × φ^1.5 |

**Note on mod 18→15:** The raw phase count for T2 and T3 is 18. The physical net count is 15 after accounting for shared overlap phases at junctions — 3-corner overlap for T3, 3-link overlap for T2 (visible in lattice QCD flux tube images). The closure law uses the net count. T4's mod=30 = 15+15 confirms the two-box ER structure.

**Notes on each toroid:**

**T0 — Plain torus (GOE, no twist):**
The only GOE entry. Time-reversal symmetry is unbroken because there is no topological twist. The GOE correction factor 30/26 applies **exclusively to T0** and arises from the angular mismatch between the geometric modular basis (cos²(30°)) and the on-shell projection (cos²(24°)):
```
λ_T0 = LU × cos²(24°)/cos²(30°) = LU × 30/26
```
This is already coded correctly as `LAM_S0` in v8.6. Do not apply this correction to any other toroid.

**T1 — Möbius parallelogram (GUE):**
The calibration base. λ = LU (no phi correction, no GOE correction). The Möbius twist breaks time-reversal symmetry → GUE. The 24° beat is the structural unit shared between T0 and T1 — this is why the photon and electron share the same mod-30 grid despite different statistics.

**T2 — HE21 tic-tac toroid, oval Hamiltonian path (GUE²):**
The switch from mod-30 to mod-15 (net) reflects the HE21 waveguide mode structure. The natural step increases to 24° = 360°/15. Lambda gains one φ^0.5 increment over T1. *Correction from v6:* an earlier version listed "natural step = 20° = 360°/18" and "9 Hamiltonian beats" — both were errors from the raw-mod description. Correct values: natural step = **24° = 360°/15**, beat count = **15**: 15 × 48° = 720° = 2×360°.

**T3 — Triangle toroid, Y Hamiltonian, triple cover (GUE³):**
Three twisted arms meeting at 120° intervals. The mod-15 net structure encodes the triangle: 6 phases per side × 3 sides = 18 total, minus 3 corner overlaps = 15 net. The H_beat is 72° (Z5* golden angle). φ(18) = 6 gives exactly 6 prime lanes per arm, consistent with the three color channels (2 lanes per color × 3 colors). Lambda = LU × φ^1.0.

**T4 — Dual mod-15 ER bridge (GUE⁴):**
Returns to mod-30 (same grid as T0/T1) but with H_beat = 48°. The dual color-anticolor structure means both chirality Hilbert spaces are simultaneously engaged, giving 4 × 360° = 1440° total closure. Lambda = LU × φ^1.5 is predicted from the phi-ladder rule and is not yet independently confirmed.

---

## The φ-Ladder Rule

The lambda values follow a geometric progression in φ^0.5 steps:

```
T1: LU × φ^0.0  (base, Möbius calibration point)
T2: LU × φ^0.5  (+0.5 per additional cover)
T3: LU × φ^1.0  (+0.5 per additional cover)
T4: LU × φ^1.5  (+0.5 per additional cover, predicted)
```

This is not inserted by hand — it emerges from the prime-lane geometry. Each additional cover multiplicity requires one extra traversal of the mod system's pentagonal sub-symmetry (Z₅* within Z₃₀*), and each such traversal costs exactly φ^0.5 in effective winding radius. The phi-ladder is the discrete renormalization group of the toroid cover hierarchy.

---

## 4.5 Spin, Dimensions, and Velocity Degrees of Freedom

The number of spatial dimensions a particle "occupies" corresponds to its toroid complexity. The spin is the closure condition of the Hamiltonian path.

**Spin as rotation count:**
A particle's spin determines how many times you must rotate it to return it to its original state:
- Spin-1 (T0, photon): rotate 360° → back to start.
- Spin-1/2 (T1, electron): one loop + 360° twist = 720° → back to start.
- Spin-3/2 (T3, Delta): one loop + 720° twist = 1080° → back to start.
- Spin-2 (graviton): would need 180° — but 180° does not close any toroid. Only exists as a correlated T4 pair.

**Dimensions from toroids (corrected v7):**

| Toroid | Closure | Spin | Spatial dims | Example |
|--------|---------|------|-------------|---------|
| T0 | 360° | 1 | 0 (time only) | EMF substrate |
| 2×T0 | 360° | 1 | 0 | Photon |
| T1 | 720° | 1/2 | 1st | Electron, light quarks |
| T2 | 720° | — | 2nd | Heavy quarks |
| T3 | 1080° | 3/2 | 3rd | Delta, Omega, baryons |
| T4 | 1440° | — | 3D + borrowed chirality | Pentaquarks, entanglement |

*Note: The v6 table listed T0 as "1D + time" and T1 as "2D effective." Both are corrected above. T0 is 0 spatial dimensions (time only, GOE). T1 opens the 1st spatial dimension. The "2D effective" label for T1 was imprecise — T1 is a 1D object that creates 2D behavior through the Möbius twist, but it occupies one spatial dimension.*
