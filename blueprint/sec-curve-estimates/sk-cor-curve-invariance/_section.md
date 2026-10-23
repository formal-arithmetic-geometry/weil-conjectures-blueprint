+++
id = "sk-cor-curve-invariance"
kind = "corollary"
title = "Proper curves over separably closed fields"
order = 1343
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isSepClosed"]
uses = ["sk-thm-curve-package", "sk-def-curve"]
tags = ["sketch"]
+++
Let $k\subseteq k'$ be separably closed fields, let $C$ be proper of
dimension at most one over $k$, and let $F$ be a classical torsion abelian
sheaf on $C_{\mathrm{proét}}$. Its natural pullback map

$$
H^q(C,F)\longrightarrow H^q(C_{k'},F|_{C_{k'}})
$$

is an isomorphism in every degree.

Here, as in $(C_7)$ of [sk-thm-curve-package], the torsion orders of $F$ are
arbitrary.
