+++
id = "theorem-cohomology-curves--7"
kind = "theorem"
title = "Cohomology of curves (7)"
name_showing = false
order = 360008
aliases = ["bp-r109-7"]
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isAlgClosed"]
+++
Let $k'/k$ be an extension of algebraically closed fields, let $C$ be a
proper scheme of finite type over $k$ with $\dim C\leq1$, let $\Lambda$
be a commutative ring, and let $F$ be a sheaf of $\Lambda$-modules on
$C_{\acute{e}t}$ whose geometric stalks are torsion abelian groups.
The pullback maps

$$
H^q(C,F)\longrightarrow H^q(C_{k'},F|_{C_{k'}})
$$

are isomorphisms for all $q\geq0$, with cohomology taken on the
underlying abelian sheaves. The statement applies to any cartesian
square presenting the base change $C_{k'}$.

By Theorem [theorem-bounded-below-cohomology-comparison], the same holds for the classical sheaf $\nu_C^*F$,
with cohomology taken on $C_{\mathrm{pro}\acute{e}t}$ and
$(C_{k'})_{\mathrm{pro}\acute{e}t}$.
