+++
id = "lemma-perverse-sheaves-curve--1"
kind = "lemma"
title = "Orthogonality and cones of monomorphisms"
name_showing = false
order = 1249001
aliases = ["bp-r386-1"]
lean = ["AlgebraicGeometry.WeilComplex.isCurvePerverseLower_iff_forall_hom_eq_zero", "AlgebraicGeometry.WeilComplex.isCurvePerverse_of_mono"]
uses = ["definition-weil-structure", "definition-perverse-sheaves-curve"]
+++
The full bounded t-structure and abelian-heart assertion is bypassed by
the Lean route, which uses the following orthogonality and cone statements.

Let $k_0$ be a finite field, let $\ell$ be a prime different from
$\operatorname{char}(k_0)$, and let $C_0$ be smooth of relative dimension
one over $k_0$. For bounded constructible Weil
$\overline{\mathbf Q}_\ell$-complexes on $C_0$, use the classes of
Definition [definition-perverse-sheaves-curve]. Then

$$
K\in{}^pD^{\ge0}
\quad\Longleftrightarrow\quad
\Hom(M,K)=0\quad\text{for every }M\in{}^pD^{\le-1}.
$$

Let $f:Q\to P$ be a monomorphism in the full subcategory of curve
perverse Weil complexes. If

$$
Q\xrightarrow{f}P\longrightarrow R\longrightarrow Q[1]
$$

is a distinguished triangle of Weil complexes, then $R$ is curve perverse.
