+++
id = "d-monodromy"
kind = "definition"
title = "Represented degree data and monodromy"
order = 3732
uses = ["lem-wf-zariski-closure-subgroup"]
lean = ["AlgebraicGeometry.Monodromy.DegreeDatum", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.frobenius", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.IsSemisimple"]
+++
A degree datum consists of a group $W$, a surjective homomorphism
$\deg:W\to\mathbf Z$, and a chosen element $\gamma$ of degree $1$.
Put $P=\ker(\deg)$; every $w$ has the form $u\gamma^{\deg w}$ with
$u\in P$. A represented datum adds, for a field $k$ and $n\ge0$, a
representation $\rho:W\to\operatorname{GL}_n(k)$ on $V=k^n$. Its arithmetic and
geometric monodromy groups are the reduced Zariski closures, as closed
subgroup schemes of $\operatorname{GL}_n$ over $k$,

$$
G=\overline{\rho(W)},\qquad H=\overline{\rho(P)},\qquad F=\rho(\gamma).
$$

A semisimple datum means that $V$ is a semisimple $W$-representation.
The chosen element is also written $s$, so that $F=\rho(s)$. A
*Weil representation* of the degree datum is a finite-dimensional
representation of $W$ over $k$; a choice of basis makes it a
represented datum.

Both closures are closed subgroups by [lem-wf-zariski-closure-subgroup].
