+++
id = "lem-ag-equal-dimension-subgroup"
kind = "lemma"
title = "A closed subgroup of full dimension is everything"
order = 2677
uses = ["def-wf-algebraic-components", "lem-wf-same-lie-closed-subgroup"]
+++
Let $G\subseteq\operatorname{GL}(V)$ be a connected closed matrix group
over $\overline{\mathbf Q}_\ell$ (connected in the sense of
[def-wf-algebraic-components]), and let $J\subseteq G$ be a closed
subgroup with $\dim J=\dim G$. Then $J=G$.

## Proof

By the first assertion of [lem-wf-same-lie-closed-subgroup], the
connected closed matrix group $G$ is irreducible. The dimension of the
closed subset $J$ is the maximum of the dimensions of its finitely many
irreducible components, so some irreducible component $J_1$ of $J$ has
$\dim J_1=\dim G$. In the irreducible finite-type variety $G$, a proper
closed irreducible subset has strictly smaller dimension; hence the
closed irreducible subset $J_1$ equals $G$. Thus $G=J_1\subseteq J
\subseteq G$, and $J=G$.
