+++
id = "def-weil-pbc-strict-henselian-setup"
kind = "definition"
title = "Strictly henselian setup"
order = 1586
lean = ["AlgebraicGeometry.Etale.projectiveLineClosedFibreRestriction"]
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-henselian-terminology", "def-weil-pbc-inverse-image"]
+++
Let $\Lambda$ be a commutative ring and $(A,\mathfrak m)$ a local ring (in the
application strictly henselian [def-weil-pbc-henselian-terminology]); put
$S=\operatorname{Spec}A$, $s=\operatorname{Spec}(A/\mathfrak m)$,
$X=\mathbf P^1_S$, and $X_0=\mathbf P^1_s$, the closed fibre. For an etale
[def-weil-pbc-etale-site] sheaf $F$ of $\Lambda$-modules on $X$, write $F_0$ for
its inverse image [def-weil-pbc-inverse-image] on $X_0$ and let

$$
 \operatorname{res}_F:\Gamma(X,F)\longrightarrow\Gamma(X_0,F_0)
$$

be restriction, i.e. the pullback of global sections along $X_0\to X$.
