+++
id = "cor-galois-open-subgroups"
kind = "theorem"
title = "Open subgroups and finite etale covers"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.galois_openSubgroups", "AlgebraicGeometry.Scheme.FiniteEtale.exists_iso_fiber_map_eq_iff"]
order = 2792
tags = ["latex:corollary"]
uses = ["def-galois-fibre-functor", "def-galois-object", "lem-galois-transitive", "thm-galois-fundamental"]
+++
Let $Y$ be connected with geometric point $\bar y$. For a connected
finite etale cover $P$ of $Y$ and a point $x\in P_{\bar y}$, the
stabilizer of $x$ in $\pi_1(Y,\bar y)$ is an open subgroup, and every
open subgroup arises in this way. Assigning to $(P,x)$ this stabilizer
is a bijection between the isomorphism classes of pointed connected
finite etale covers $(P,x)$ of $Y$ (isomorphisms over $Y$ carrying the
point to the point) and the open subgroups of $\pi_1(Y,\bar y)$.
Forgetting the point, the stabilizers of the points of $P_{\bar y}$ form
one conjugacy class, and $P\mapsto$ this class is a bijection between
the isomorphism classes of connected finite etale covers of $Y$ and the
conjugacy classes of open subgroups of $\pi_1(Y,\bar y)$. The degree of
$P$ over $Y$ is the index of the stabilizer of any point of $P_{\bar y}$.
