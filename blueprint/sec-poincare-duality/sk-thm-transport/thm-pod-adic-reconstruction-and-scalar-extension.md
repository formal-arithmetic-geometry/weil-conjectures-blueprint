+++
id = "thm-pod-adic-reconstruction-and-scalar-extension"
kind = "theorem"
title = "Adic reconstruction and scalar extension"
order = 2450
uses = ["def-pod-conventions", "def-pod-derived-poincare-pairing", "def-weil-pbc-adic-coefficient-datum", "lem-weil-pbc-reconstruction-uniform-tower", "thm-pod-derived-poincare-duality", "thm-pod-finite-reduction"]
+++
Let $X/k$ be smooth and geometrically connected as in
the Poincare duality conventions, and
let $K$ be a derived-complete
site-perfect $\mathcal O_E$-complex whose reductions
$K_n=K\otimes^L A_{E,n}$ form a normalized system with common
constructible and finite-Tor bounds. Assume the admissible structure
morphism and coefficient conventions used for the Poincare pairing. The finite-level pairings $\beta _{K_n}$ of [def-pod-derived-poincare-pairing] form a morphism of normalized systems (by [thm-pod-finite-reduction]), and they induce the $\mathcal O_E$-valued derived Poincare pairing

$$
R\Gamma _c(X,K)\otimes ^L_{\mathcal O_E}R\Gamma \bigl(X,K^\vee (d)\bigr)[2d] \longrightarrow \mathcal O_E,
$$

perfect in the sense of the uniform-tower reconstruction of [lem-weil-pbc-reconstruction-uniform-tower]: the inverse of its adjoint is the canonical isomorphism

$$
R\Gamma _c(X,K)^\vee \xrightarrow {\  \sim \  } R\Gamma \bigl(X,K^\vee (d)\bigr)[2d]
$$

over $\mathcal O_E$. Localization at $\varpi _E$ and finite coefficient-field extension carry this pairing, its adjoint, every degree-indexing map, the relative form, and all Frobenius squares to their counterparts over the extended coefficient field.
