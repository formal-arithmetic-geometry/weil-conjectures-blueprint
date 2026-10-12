+++
id = "prop-av-tate-no-frobenius-fixed"
kind = "theorem"
title = "No Frobenius-fixed vectors on the Tate module of an abelian variety"
order = 2902
uses = ["d-ab-field", "def-sc-abelian-variety", "def-tate-module-abelian-group", "lem-tate-module-no-fixed"]
tags = ["latex:proposition"]
+++
Let $A_0$ be an abelian variety over the finite field $k_0$ of [d-ab-field],
$A=A_0(\bar k)$, and $\ell\ne p$. Its rational Tate module has no nonzero
vector fixed by geometric Frobenius:

$$
(V_\ell A)^F=0.
$$

More precisely, with $T_\ell A$, $V_\ell A$ the Tate modules of the abelian
group $A$ ([def-tate-module-abelian-group]), on which the arithmetic
Frobenius $\sigma$ and $F=\sigma^{-1}$ act coordinatewise, one has
$(T_\ell A)^\sigma=(T_\ell A)^F=0$ and $(V_\ell A)^\sigma=(V_\ell A)^F=0$.
