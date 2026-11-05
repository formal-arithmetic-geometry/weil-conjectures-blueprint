+++
id = "theorem-smooth-base-change-classical-torsion--1"
kind = "theorem"
title = "Smooth base change for torsion étale module sheaves"
name_showing = false
order = 662001
aliases = ["bp-r200-1"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_smooth"]
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves"]
+++
In the cartesian square (8.1), suppose $g$ is smooth and $f$ is
quasi-compact and quasi-separated. Let $\Lambda$ be a commutative ring
and let $F$ be a sheaf of $\Lambda$-modules on $X_{\acute{e}t}$.
Suppose that every element of every geometric stalk of $F$ is killed
by a positive integer $n$ invertible on $Y$; the integer may depend
on the element. Then for every $q\in\mathbf Z$ the degree-$q$ base change
map induced by [definition-derived-base-change-map]

$$
g^{-1}R^qf_*F\longrightarrow R^qf'_*g'^{-1}F
$$

is an isomorphism on $Y'_{\acute{e}t}$.
