+++
id = "sk-cor-curve-invariance"
kind = "lemma"
title = "Extension of a separably closed ground field"
order = 201
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isSepClosed"]
uses = ["sk-thm-curve-package"]
tags = ["sketch"]
+++
Let $k\subseteq k'$ be separably closed fields, let $C$ be proper over $k$
with $\dim C\leq1$, and let $F$ be a classical torsion abelian sheaf
on $C_{\mathrm{pro}\acute{e}t}$. Then the natural map

$$
H^q(C,F)\xrightarrow{\sim}H^q(C_{k'},F|)
\qquad(q\geq0)
$$

is an isomorphism.
