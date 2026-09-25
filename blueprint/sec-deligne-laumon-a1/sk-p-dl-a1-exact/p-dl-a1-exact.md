+++
id = "p-dl-a1-exact"
kind = "theorem"
title = "Exactness at a fixed pure weight"
order = 2987
uses = ["cor-wf-inertia-invariants", "cor-wf-unramified-boundary-purity", "def-wf-middle-extension", "lem-a1-middle-extension-dual-triangle", "lem-a1-middle-extension-duality", "lem-wf-boundary-coinvariant-lower-bound", "lem-wf-boundary-semicontinuity", "lem-wf-euler-product-middle-extension", "lem-wf-local-inertia-finite-parts", "lem-wf-local-monodromy-quasi-unipotent", "lem-wf-point-count-linear-growth", "lem-wf-unipotent-invariants-kernel"]
tags = ["latex:proposition"]
+++
For a short exact sequence $0\to F_1\to F\to F_2\to0$ of lisse
Weil sheaves, all pure of the same weight $w$, ordinary middle
extension is exact:

$$
0\longrightarrow j_*F_1\longrightarrow j_*F
\longrightarrow j_*F_2\longrightarrow0.
$$

## Proof

The possible failure of surjectivity is the connecting map
$\delta:j_*F_2\to R^1j_*F_1$, which vanishes on the open.
At a missing point the source has weights at most $w$ by
semicontinuity. The dual $F_1^\vee$ has weight $-w$, so its
middle-extension stalk has weights at most $-w$. Local duality
identifies $(R^1j_*F_1)_{\bar s}$ with the dual of that stalk,
twisted by $(-1)$; its weights are at least $w+2$.
A Frobenius-equivariant map across this strict weight gap is zero:
its image would have to satisfy both incompatible bounds.
Thus $\delta$ vanishes on every geometric stalk, proving exactness.

Uses: [def-wf-middle-extension], [lem-a1-middle-extension-dual-triangle], [lem-a1-middle-extension-duality], [cor-wf-inertia-invariants], [cor-wf-unramified-boundary-purity], [lem-wf-boundary-coinvariant-lower-bound], [lem-wf-boundary-semicontinuity], [lem-wf-euler-product-middle-extension], [lem-wf-local-inertia-finite-parts], [lem-wf-local-monodromy-quasi-unipotent], [lem-wf-point-count-linear-growth], [lem-wf-unipotent-invariants-kernel]
