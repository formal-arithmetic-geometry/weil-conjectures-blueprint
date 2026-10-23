+++
id = "lem-wf-point-count-linear-growth"
kind = "lemma"
title = "Linear growth of the point count on an affine curve"
lean = ["AlgebraicGeometry.Scheme.Hom.exists_pointCount_le_mul_pow"]
order = 3898
uses = ["def-weil-pbc-scheme-conventions", "lem-zl-noether-normalization-dimension"]
+++
Let $U_0$ be a smooth affine curve over $k_0=\mathbf F_q$ (in the
separated finite-type
conventions of [def-weil-pbc-scheme-conventions]) and let
$k_n=\mathbf F_{q^n}$. Then there is a constant $d\ge1$ such that

$$
\#U_0(k_n)\le d\,q^n\qquad(n\ge1).
$$
