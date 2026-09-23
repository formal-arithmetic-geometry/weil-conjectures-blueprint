+++
id = "ordered-dependency-spine"
kind = "section"
title = "Ordered dependency spine"
order = 1403
+++
1. Construct the single global unit–Cartesian-identification–counit mate.
1. Prove the finite-morphism fibre formula and exactness.
1. Prove composition stability and proper-surjective cancellation.
1. Use Chow reduction and the finite symmetric-product map to reduce to
$\mathbf P^1$.
1. Prove the strict-henselian $\mathbf P^1$ comparison from degree zero,
affine Gabber comparison, and finite-etale torsor lifting.
1. Identify the global stalk map using strict henselization and proper-curve
invariance under separably closed extension.
1. Assemble prime and arbitrary torsion coefficients, then pass to $D^+$ by
a bounded-below hypercohomology spectral sequence.
1. Transport finite levels to the pro-etale site.
1. Reconstruct completed coefficients by perfect reduction and
$R\varprojlim$.
1. Verify naturality, identity, pasting, and typed Frobenius coherence.

**Detailed realization.** Steps 2--7 of this list (S1--S7) are now carried out
in full by the eighteen subsections merged in from chapter 5 of
`weil_conjectures_detailed.tex`; see [chap-proper-base-change] for the
step-by-step table. Step 1, the global mate, is
[def-weil-pbc-derived-exchange-detailed] of [foundations], which the detailed
chapter takes as given rather than constructing. Steps 8--10 --- pro-etale
transport, derived completion, and the complete comparison --- have no
counterpart in chapter 5 and still rest on the route's own statements; their
detailed source is chapter 6, not yet imported.

**Status.** The proof order above is a reduction order. Formal status may be
promoted only in the reverse dependency direction: exact leaves first, then
S0–S7, then finite PBC, and only later the completed and compact-support
exports.
