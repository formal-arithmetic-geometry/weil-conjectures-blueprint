+++
id = "definition-torsion-sheaves--3"
kind = "lemma"
title = "Filtered-colimit criterion"
order = 340004
aliases = ["bp-r103-3"]
lean = ["AlgebraicGeometry.Scheme.IsTorsionModuleSheaf.exists_isColimit", "AlgebraicGeometry.Scheme.isTorsionAbelianSheaf_characterizations", "AlgebraicGeometry.Scheme.isTorsionModuleSheaf_iff_isTorsion", "AlgebraicGeometry.Scheme.isTorsionSheaf_iff_isTorsion"]
uses = ["definition-torsion-sheaves--1"]
+++
Let $T$ be a scheme and let $F$ be a sheaf of abelian groups on
$T_{\acute{e}t}$. The following conditions are equivalent:

1. The canonical map
   $$
   \varinjlim_{n\geq1}F[n]\longrightarrow F
   $$
   is an isomorphism, where positive integers are ordered by divisibility
   and $F[n]$ is as in [definition-torsion-sheaves--2].
2. Every section of $F$ is locally killed by a positive integer on an
   étale covering; the integer may vary between members of the covering.
3. For every algebraically closed field $\Omega$ and every geometric
   point $\operatorname{Spec}\Omega\to T$, the stalk of $F$ is a torsion
   abelian group.

Condition 2 is also equivalent to torsion in the sense of
[definition-torsion-sheaves--1], using all separably closed geometric
points.

If $\Lambda$ is a commutative ring and $F$ is a sheaf of
$\Lambda$-modules on $T_{\acute{e}t}$, then $F$ is torsion if and only if
its underlying abelian sheaf satisfies condition 2. In this case there
exist a small filtered category $J$ and a diagram $(D_j)_{j\in J}$ of
sheaves of $\Lambda$-modules, with colimit $F$, such that for each $j$
there is a positive integer $n_j$ with $n_j\,\operatorname{id}_{D_j}=0$.
