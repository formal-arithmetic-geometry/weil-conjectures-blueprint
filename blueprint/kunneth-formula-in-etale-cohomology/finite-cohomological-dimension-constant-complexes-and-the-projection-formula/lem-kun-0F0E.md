+++
id = "lem-kun-0F0E"
kind = "lemma"
title = "Tensor with a constant complex over $\\mathbf Z$"
order = 6100
lean = ["AlgebraicGeometry.Etale.RGamma_tensor_constant_Z_iso"]
uses = ["def-kun-constant-sheaf", "def-kun-derived-tensor", "def-kun-truncations"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme. For
$E\in\Dplus(X_{\Et})$ and $K\in\Dplus(\mathbf Z)$, the canonical map
$$
R\Gamma(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z}K\longrightarrow
R\Gamma\bigl(X_{\Et},E\otimes^{\mathbf L}_{\mathbf Z}\underline{K}\bigr)
$$
is an isomorphism.

## Proof

Both sides are triangulated functors in $K\in\Dplus(\mathbf Z)$, and for
$K=\mathbf Z$ placed in degree zero the map is the unit constraint of the
tensor product, hence an isomorphism; the same holds for every bounded
complex of free $\mathbf Z$-modules, both sides being compatible with finite
direct sums and shifts on the nose.

For a general bounded-below $K$ write $K=\varinjlim_N\sigma_{\ge-N}K$ as the
filtered colimit of its stupid truncations ([def-kun-truncations]); since
$E$ is bounded below, in each cohomological degree the tensor product
$R\Gamma(X_{\Et},E)\otimes_{\mathbf Z}K$ involves only finitely many degrees
of $K$ below any bound, so the horizontal maps are the colimits of the
isomorphisms for the truncations, and likewise for
$R\Gamma(X_{\Et},E\otimes_{\mathbf Z}\underline{K})$ because
$\underline{K}$ is the colimit of the $\underline{\sigma_{\ge-N}K}$ and
cohomology commutes with filtered colimits of complexes.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-etale-cohomology
