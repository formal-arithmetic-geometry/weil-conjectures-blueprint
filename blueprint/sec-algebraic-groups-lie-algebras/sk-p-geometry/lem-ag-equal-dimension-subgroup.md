+++
id = "lem-ag-equal-dimension-subgroup"
kind = "lemma"
title = "A closed subgroup of full dimension is everything"
lean = ["AlgebraicGeometry.isIso_left_of_topologicalKrullDim_eq", "Matrix.GeneralLinearGroup.eq_of_le_of_ringKrullDim_eq"]
order = 3898
uses = ["lem-ag-cartier-reduced", "lem-wf-affine-dimension-drop", "lem-wf-algebraic-component-cosets"]
+++
Let $G$ be a connected group scheme of finite type over an algebraically
closed field $L$ of characteristic zero, and let $J\subseteq G$ be a
closed subgroup scheme with $\dim J=\dim G$. Then $J=G$.

*Complement.* If $G\subseteq\operatorname{GL}(V)$ is an irreducible
closed matrix group over $L$ and $J\subseteq G$ is a closed subgroup with
$\dim J=\dim G$, then $J=G$.
