+++
id = "sk-thm-picard-twist"
kind = "lemma"
title = "Translating into the chart"
order = 841
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-thm-picard-perfect", "sk-thm-picard-rr", "sec-abelian-varieties", "sec-nagata-compactification", "sk-def-picard-pic", "sk-prop-picard-pic-split", "sk-thm-picard-f-representable"]
lean = ["AlgebraicGeometry.Scheme.exists_isInvertible_twist"]
tags = ["sketch"]
+++
Let $C/k$ be a smooth projective geometrically connected curve, and
suppose that $k$ is algebraically closed. For every field extension $K/k$
and every invertible sheaf $\cL$ on $C_K$, there is an invertible sheaf
$\cM_0$ on $C$ such that

$$
h^0(C_K,\cL\otimes\cM_{0,K})=1,
\qquad H^1(C_K,\cL\otimes\cM_{0,K})=0.
$$

(The same holds, with the same proof, for $k$ separably closed and $C$ a
connected smooth proper curve over $k$: the only input about $k$ is that
$C(k)$ is infinite, [det-prop-picard-dense-points].)
