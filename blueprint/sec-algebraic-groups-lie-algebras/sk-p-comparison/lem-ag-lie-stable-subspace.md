+++
id = "lem-ag-lie-stable-subspace"
kind = "lemma"
title = "Group-invariant and Lie-invariant subspaces agree"
lean = ["AlgebraicGeometry.GeneralLinearGroup.forall_zeroLocus_iff_forall_lieSubalgebra", "AlgebraicGeometry.GeneralLinearGroup.forall_mem_zeroLocus_iff_forall_mem_lieSubalgebra", "AlgebraicGeometry.GeneralLinearGroup.forall_mulVec_mem_iff_forall_lieSubalgebra"]
order = 2841
uses = ["def-wf-algebraic-components", "def-wf-algebraic-representations", "def-wf-lie-algebra-derivation", "lem-ag-cartier-reduced", "lem-wf-same-lie-closed-subgroup"]
+++
Let $H\subseteq\operatorname{GL}(V)$ be a connected closed matrix group
over $k=\overline{\mathbf Q}_\ell$ (connected in the sense of
[def-wf-algebraic-components]), with Lie algebra
$\mathfrak h=\operatorname{Lie}(H)$ as in
[def-wf-lie-algebra-derivation], and let $r:H\to\operatorname{GL}(M)$ be
a rational representation, i.e. an algebraic-group module in the sense
of [def-wf-algebraic-representations]. Its differential
$dr:\mathfrak h\to\operatorname{End}(M)$ is defined by

$$
r(1+\varepsilon X)=1+\varepsilon\,dr(X)
\qquad\text{in }\operatorname{GL}(M)(k[\varepsilon]/\varepsilon^2),
\quad X\in\mathfrak h .
$$

Then a subspace $U\subseteq M$ is $H$-invariant if and only if
$dr(X)U\subseteq U$ for every $X\in\mathfrak h$.
