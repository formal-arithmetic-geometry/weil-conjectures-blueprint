+++
id = "lem-wf-algebraic-component-cosets"
kind = "lemma"
title = "Identity component, cosets, and the finite component group"
lean = ["AlgebraicGeometry.finite_connectedComponents", "AlgebraicGeometry.GrpObj.isClopen_connectedComponent_onePoint", "AlgebraicGeometry.GrpObj.irreducibleSpace_identityComponent", "AlgebraicGeometry.GrpObj.finiteIndex_range_identityComponentι", "AlgebraicGeometry.GrpObj.image_mulLeft_connectedComponent_onePoint", "Matrix.GeneralLinearGroup.isClopen_connectedComponent_zeroLocus"]
order = 3686
uses = ["def-sc-group-scheme-translate", "def-wf-algebraic-components", "lem-ag-cartier-reduced", "lem-sc-translation-automorphism", "lem-wf-affine-noetherian-components", "lem-wf-affine-nullstellensatz-vanishing", "lem-wf-smooth-components-disjoint"]
+++
Let $G$ be a group scheme of finite type over an algebraically closed
field $L$ of characteristic zero, and let $G^\circ$ be the connected
component of $G$ containing the identity. Then $G$ has finitely many
connected components. The identity component $G^\circ$ is open, closed
and irreducible, and it is a normal subgroup of $G$. The connected
components of $G$ are exactly the pairwise disjoint translates $gG^\circ$
with $g\in G(L)$, and multiplication of cosets makes

$$
\pi_0(G)=G(L)/G^\circ(L)
$$

a finite group.

*Complement.* For a closed algebraic subgroup
$H\subseteq\operatorname{GL}(V)$ and its identity component $H^\circ$ of
[def-wf-algebraic-components], $H^\circ$ is a closed, open, normal
subgroup, the connected components of $H$ are the cosets $hH^\circ$, and
$\pi_0(H)=H/H^\circ$ is a finite group.
