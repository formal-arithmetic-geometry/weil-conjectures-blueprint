+++
id = "lemma-representability-picard-functor--1"
kind = "lemma"
title = "Representability from translated open charts"
name_showing = false
order = 1544001
aliases = ["bp-r481-1"]
lean = ["AlgebraicGeometry.isRepresentable_of_representable_open_subfunctor", "AlgebraicGeometry.exists_isOpenImmersion_of_representable_open_subfunctor"]
uses = []
+++
Let $k$ be a field and let $G$ be a presheaf of groups on $k$-schemes.
Work in a fixed universe containing $k$ and the schemes, and suppose
that each $G(T)$ is small in this universe. Suppose that $G$ is a
Zariski sheaf and that $F\subset G$ is a subfunctor represented by a
$k$-scheme $A$, whose inclusion is representable by open immersions.
Assume that for every field extension $K/k$ and every $g\in G(K)$
there is an $m\in G(k)$ such that

$$
m_Kg\in F(K).
$$

Then $G$ is represented by a group scheme over $k$.

Moreover, the open-immersion and field-extension hypotheses alone
imply the following: if a $k$-scheme $A'$ represents $G$, every point
of $A'$ lies in the image of an open immersion $A\to A'$ over $k$.
Thus these copies of $A$ cover $A'$; this assertion does not require
the smallness or sheaf hypotheses.
