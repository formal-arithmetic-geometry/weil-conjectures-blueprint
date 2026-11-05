+++
id = "theorem-smooth-base-change-classical-torsion-2--1"
kind = "theorem"
title = "Étale smooth base change for bounded below torsion complexes"
name_showing = false
order = 693001
aliases = ["bp-r208-1"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_app_of_smooth_of_isTorsionSheafOfInvertibleOrder"]
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves"]
+++
For bounded below complexes, Lean uses the following étale formulation
in place of the classical pro-étale statement.

In (8.1), let $g$ be smooth and $f$ quasi-compact and
quasi-separated. Let $\Lambda$ be a commutative ring and let

$$
K\in D^+(X_{\acute{e}t},\Lambda).
$$

Suppose that, for every $j\in\Z$, every element of every geometric
stalk of $H^j(K)$ is killed by some positive integer $n$ invertible on
$Y$, that is, a unit in $\Gamma(Y,\mathcal O_Y)$. The integer may depend
on the element and on $j$; no common annihilator of $\Lambda$ is required.
Then the derived base change map of [definition-derived-base-change-map]

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+(Y'_{\acute{e}t},\Lambda)$.
