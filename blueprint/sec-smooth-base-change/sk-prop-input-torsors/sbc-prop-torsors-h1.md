+++
id = "sbc-prop-torsors-h1"
kind = "theorem"
title = "Torsors and etale $H^1$"
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_sheafTorsor", "AlgebraicGeometry.Scheme.EtaleTorsor.toSheafTorsor"]
order = 1464
tags = ["latex:proposition"]
uses = ["def-galois-fibre-functor", "def-weil-pbc-finite-torsors", "lem-fet-galois-category", "lem-galois-axioms", "thm-galois-fundamental", "thm-galois-lc-etale", "thm-galois-torsor-h1"]
+++
Let $Y$ be a scheme and $M$ a finite abelian group. Then there is a
canonical bijection, natural in $(Y,M)$,

$$
\operatorname{Tor}^1(Y,M)\xrightarrow{\ \sim\ }H^1(Y_{\Et},\underline M)
$$

between the pointed set of isomorphism classes of $M$-torsors of
[def-weil-pbc-finite-torsors] and $H^1(Y_{\Et},\underline M)$, and an
$M$-torsor is the same thing as a finite etale $Y$-scheme, surjective over
$Y$, with a simply transitive $M$-action. Moreover, let $Y$ be connected
with geometric point $\bar y$. For an $M$-torsor $P$, viewed as a finite
etale $Y$-scheme, and $p\in|P_{\bar y}|$, let
$f_P:\pi_1(Y,\bar y)\to M$ be defined by $g\cdot p=p+f_P(g)$; it is
a continuous homomorphism independent of $p$ and of $P$ within its
isomorphism class. Then $P$ is connected — that is, a Galois cover with
group $M$ — exactly when $f_P$ is surjective.
