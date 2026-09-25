+++
id = "lem-ag-commuting-product-closed"
kind = "lemma"
title = "The product of two commuting connected closed subgroups is closed"
order = 2678
uses = ["def-wf-algebraic-components", "lem-wf-dominant-affine-open-piece", "lem-wf-same-lie-closed-subgroup"]
+++
Let $A,B\subseteq\operatorname{GL}(V)$ be connected closed matrix groups
over $\overline{\mathbf Q}_\ell$ such that every element of $A$ commutes
with every element of $B$. Then $AB$ is a connected closed subgroup of
$\operatorname{GL}(V)$.

## Proof

Let

$$
S=\overline{AB}^{\,\mathrm{Zar}}\subseteq\operatorname{GL}(V).
$$

Because $A$ and $B$ commute, $AB$ is a subgroup.
Continuity of multiplication and inversion shows that its closure
$S$ is again a subgroup: for fixed $y\in AB$ the closed condition
$xy\in S$ holds on $AB$, hence on $S$; then for fixed $x\in S$ the closed
condition $xy\in S$ holds on $AB$, hence on $S$; inversion is the same
argument. It is connected and contains the identity (connectedness in
the sense of [def-wf-algebraic-components]).

The multiplication morphism

$$
A\times B\longrightarrow S,\qquad(a,b)\longmapsto ab,
$$

is dominant by the definition of $S$. The source (a connected closed
matrix group, block-diagonal in $\operatorname{GL}(V\oplus V)$) and the
target are irreducible by [lem-wf-same-lie-closed-subgroup], so
[lem-wf-dominant-affine-open-piece] gives a nonempty open subset
$U\subseteq S$ contained in $AB$. Now

$$
U^{-1}U=\bigcup_{u\in U}u^{-1}U
$$

is an open neighbourhood of the identity contained in the subgroup
$AB$. Its left translates show that $AB$ is open in
$S$; the other cosets show that its complement is open as well.
Thus $AB$ is closed in $S$, and its density forces

$$
S=AB.
$$

Being the image of the connected space $A\times B$, it is connected.
