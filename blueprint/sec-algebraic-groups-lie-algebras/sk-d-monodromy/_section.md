+++
id = "sk-d-monodromy"
kind = "definition"
title = "Represented degree data and monodromy"
order = 2499
uses = ["sk-d-geometry", "sk-d-linear"]
lean = ["AlgebraicGeometry.Monodromy.DegreeDatum", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.frobenius", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.IsSemisimple"]
tags = ["sketch"]
+++
A degree datum consists of a group $W$, a surjective homomorphism
$\deg:W\to\mathbf Z$, and a chosen element $\gamma$ of degree $1$.
Put $P=\ker(\deg)$; every $w$ has the form $u\gamma^{\deg w}$ with
$u\in P$. A represented datum adds, for a field $k$ and $n\ge0$, a
representation $\rho:W\to\GL_n(k)$ on $V=k^n$. Its arithmetic and
geometric monodromy groups are the reduced Zariski closures, as closed
subgroup schemes of $\GL_n$ over $k$,

$$
G=\overline{\rho(W)},\qquad H=\overline{\rho(P)},\qquad F=\rho(\gamma).
$$

A semisimple datum means that $V$ is a semisimple $W$-representation.
