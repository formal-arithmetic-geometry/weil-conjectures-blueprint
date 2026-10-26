+++
id = "lem-ag-lie-stable-subspace"
kind = "lemma"
title = "Group-invariant and Lie-invariant subspaces agree"
lean = ["AlgebraicGeometry.GeneralLinearGroup.invariant_iff_differential_invariant", "AlgebraicGeometry.GeneralLinearGroup.forall_zeroLocus_iff_forall_lieSubalgebra", "AlgebraicGeometry.GeneralLinearGroup.forall_mem_zeroLocus_iff_forall_mem_lieSubalgebra", "AlgebraicGeometry.GeneralLinearGroup.forall_mulVec_mem_iff_forall_lieSubalgebra"]
order = 3694
uses = ["def-wf-algebraic-components", "def-wf-algebraic-representations", "def-wf-lie-algebra-derivation", "lem-ag-cartier-reduced", "lem-ag-equal-dimension-subgroup", "lem-sc-translation-automorphism", "lem-wf-affine-nullstellensatz-vanishing", "lem-wf-same-lie-closed-subgroup", "lem-wf-smooth-components-disjoint"]
+++
Let $G$ be a connected group scheme locally of finite type over an
algebraically closed field $L$ of characteristic zero, with Lie algebra
$\mathfrak g=\operatorname{Lie}(G)$ as in
[def-wf-lie-algebra-derivation], and let $r:G\to\operatorname{GL}(M)$ be
a rational representation on a finite-dimensional $L$-vector space $M$,
with differential $dr:\mathfrak g\to\operatorname{End}(M)$. Then a
subspace $U\subseteq M$ satisfies $r(g)U\subseteq U$ for every
$g\in G(L)$ if and only if $dr(X)U\subseteq U$ for every
$X\in\mathfrak g$.

*Complement.* Let $H\subseteq\operatorname{GL}(V)$ be a connected closed
matrix group over $L$ (connected in the sense of
[def-wf-algebraic-components]), with Lie algebra
$\mathfrak h=\operatorname{Lie}(H)$ computed by dual numbers, and let
$r:H\to\operatorname{GL}(M)$ be an algebraic-group module in the sense
of [def-wf-algebraic-representations], with differential defined by

$$
r(1+\varepsilon X)=1+\varepsilon\,dr(X)
\qquad\text{in }\operatorname{GL}(M)(L[\varepsilon]/\varepsilon^2),
\quad X\in\mathfrak h .
$$

Then a subspace $U\subseteq M$ is $H$-invariant if and only if
$dr(X)U\subseteq U$ for every $X\in\mathfrak h$.
