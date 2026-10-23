+++
id = "sk-prop-av-ntorsion-etale"
kind = "proposition"
title = "The $n$-torsion of an abelian variety is étale"
lean = ["AlgebraicGeometry.etale_torsionSubgroupScheme", "AlgebraicGeometry.isFinite_torsionSubgroupScheme", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme", "AlgebraicGeometry.nonempty_addEquiv_torsionBy", "AlgebraicGeometry.torsionByEquiv"]
order = 611
uses = ["sk-def-av", "sk-def-av-mult-n", "sk-prop-av-connected-order", "sk-prop-av-divisible", "sk-prop-av-divisible-structure", "sk-prop-av-finite-etale-points", "sk-prop-av-isogeny"]
tags = ["sketch"]
+++
Let $A$ be an abelian variety of dimension $g$ over a field $k$ and
let $n\ge1$ be prime to $\operatorname{char}k$. Then $A[n]$ is a finite
étale group scheme over $k$. If moreover $k$ is algebraically closed,
the canonical base change map $A[n](k)\to A[n](k')$ is a bijection for
every extension $k\subseteq k'$ of algebraically closed fields, and

$$
A[n](k)=A(k)[n]\cong(\Z/n\Z)^{2g}.
$$
