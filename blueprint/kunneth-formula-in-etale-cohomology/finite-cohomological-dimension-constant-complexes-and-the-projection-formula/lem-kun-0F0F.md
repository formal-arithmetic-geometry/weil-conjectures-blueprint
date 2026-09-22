+++
id = "lem-kun-0F0F"
kind = "lemma"
title = "Projection formula, integer coefficients"
order = 6101
lean = ["AlgebraicGeometry.Etale.IsProper.projectionFormula_Z_isIso"]
uses = ["def-kun-torsion-invertible", "def-kun-derived-tensor", "def-kun-projection-formula-map", "lem-kun-derived-tensor-triangulated"]
+++
Let $f:X\to Y$ be a proper morphism, let $E\in\Dplus(X_{\Et})$ have torsion
cohomology [def-kun-torsion-invertible], and let $K\in\Dplus(Y_{\Et})$. Then
the canonical projection-formula map
$$
\mathrm{PF}_f(E,K):\quad Rf_*E\otimes^{\mathbf L}_{\mathbf Z}K\longrightarrow
Rf_*(E\otimes^{\mathbf L}_{\mathbf Z}f^{-1}K)
$$
is an isomorphism in $\Dplus(Y_{\Et})$.

## Proof

Both sides of [def-kun-projection-formula-map] are triangulated functors in
$K\in\Dplus(Y_{\Et})$, and for $K=\mathbf Z$ in degree zero the map is the
identity constraint $Rf_*E\otimes_{\mathbf Z}\mathbf Z\to Rf_*E$, an
isomorphism; the same holds for a bounded-below complex $F$ of free
$\mathbf Z$-module sheaves, since both sides commute with finite direct sums
and shifts and $f^{-1}$ of a free sheaf is free (the inverse image is
exact).

For a general $K\in\Dplus(Y_{\Et})$ choose a quasi-isomorphism $F\to K$ from
a bounded-below complex of free sheaves: such an $F$ exists by the standard
Cartan–Eilenberg construction (in each degree the kernel of the previous map
is a quotient of a direct sum of copies of $\mathbf Z_Y$). Then $F$ is
K-flat, so $Rf_*E\otimes^{\mathbf L}_{\mathbf Z}K=Rf_*E\otimes F$ and
$E\otimes^{\mathbf L}_{\mathbf Z}f^{-1}K=E\otimes f^{-1}F$, and the
comparison of the previous paragraph is the assertion.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-inverse-image
