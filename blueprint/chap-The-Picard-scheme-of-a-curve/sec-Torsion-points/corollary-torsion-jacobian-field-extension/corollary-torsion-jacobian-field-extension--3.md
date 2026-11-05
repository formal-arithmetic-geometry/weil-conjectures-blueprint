+++
id = "corollary-torsion-jacobian-field-extension--3"
kind = "corollary"
title = "Divisibility of the Jacobian points"
order = 1561006
aliases = ["bp-r487-3"]
lean = ["AlgebraicGeometry.Scheme.surjective_pow_picardZero", "AlgebraicGeometry.surjective_npow_points"]
+++
For every abelian variety $A/k$ and every integer $m>0$,
multiplication by $m$ on $A(k)$ is surjective. No invertibility
assumption on $m$ is needed.

In particular, $J(C)(k)$ is divisible. Under its identification
with $\operatorname{Pic}^0(C)=\ker(\deg)$, this says that

$$
\operatorname{Pic}^0(C)\longrightarrow\operatorname{Pic}^0(C),
\qquad \cL\longmapsto\cL^{\otimes m}
$$

is surjective for every $m>0$.
