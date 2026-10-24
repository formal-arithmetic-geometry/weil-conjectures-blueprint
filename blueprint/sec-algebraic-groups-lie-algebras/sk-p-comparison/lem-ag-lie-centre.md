+++
id = "lem-ag-lie-centre"
kind = "lemma"
title = "Lie algebra of the centre"
lean = ["AlgebraicGeometry.GeneralLinearGroup.forall_commute_iff_forall_lieSubalgebra", "AlgebraicGeometry.GeneralLinearGroup.mem_lieSubalgebra_center_iff", "AlgebraicGeometry.GeneralLinearGroup.range_lieAlgebraMap_center", "AlgebraicGeometry.GeneralLinearGroup.range_lieAlgebraMap_identityComponent_center"]
order = 3713
uses = ["def-wf-lie-algebra-derivation", "def-wf-lie-radical-centre", "lem-ag-cartier-reduced", "lem-wf-algebraic-component-cosets", "lem-wf-same-lie-closed-subgroup"]
+++
Let $H\subseteq\operatorname{GL}(V)$ be a connected closed matrix group
over $\overline{\mathbf Q}_\ell$, with Lie algebra
$\mathfrak h=\operatorname{Lie}(H)$ as in
[def-wf-lie-algebra-derivation] and centre $\mathfrak z(\mathfrak h)$
as in [def-wf-lie-radical-centre]. Then, regarding the Lie algebras of
$Z(H)$ and $Z(H)^\circ$ as subspaces of $\mathfrak h$ via the
differentials of the inclusions,

$$
\operatorname{Lie}\bigl(Z(H)^\circ\bigr)=\operatorname{Lie}Z(H)=\mathfrak z(\mathfrak h).
$$
