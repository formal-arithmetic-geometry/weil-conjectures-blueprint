+++
id = "lemma-products-composites-u-admissible-blow--3"
kind = "lemma"
title = "Products and composites of $U$-admissible blow-ups (3)"
name_showing = false
order = 1433005
aliases = ["bp-r445-3"]
lean = ["AlgebraicGeometry.IsAdmissible.exists_extend", "AlgebraicGeometry.IsAdmissible.exists_extend_of_disjoint"]
uses = ["definition-admissible-blow-up--1"]
+++
Let $T$ be quasi-compact and quasi-separated, let $V\subseteq T$ be a
quasi-compact open, and let $U\subseteq V$ be an open of $T$.
Let $\mathcal J\subseteq\mathcal O_V$ be a quasi-coherent ideal of finite
type with $\mathcal J|_U=\mathcal O_U$.
There are a quasi-coherent ideal $\mathcal K\subseteq\mathcal O_T$ of
finite type with $\mathcal K|_U=\mathcal O_U$ and a morphism

$$
h:\operatorname{Bl}_{\mathcal J}(V)\longrightarrow
\operatorname{Bl}_{\mathcal K}(T)
$$

such that $b_{\mathcal K}\circ h=i\circ b_{\mathcal J}$, where
$i:V\hookrightarrow T$ is the inclusion and $b_{\mathcal K}$, $b_{\mathcal J}$ are the
blow-up morphisms, and the resulting square with bottom map $i$ is
cartesian. Thus the blow-up of $\mathcal K$ restricts over $V$ to the
given blow-up. The open $U$ need not be quasi-compact.

There is also a version without the containment $U\subseteq V$.
If $U,V\subseteq T$ are both quasi-compact opens and
$\mathcal J|_{U\cap V}=\mathcal O_{U\cap V}$, the same conclusion holds:
the extended center avoids all of $U$ and the square over $V$ is
cartesian.
