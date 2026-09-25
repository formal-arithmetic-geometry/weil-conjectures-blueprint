+++
id = "prop-av-tate-no-frobenius-fixed"
kind = "theorem"
title = "No Frobenius-fixed vectors on the Tate module of an abelian variety"
order = 2720
uses = ["d-ab-field", "def-sc-abelian-variety", "def-tate-module-abelian-group", "lem-tate-module-no-fixed"]
tags = ["latex:proposition"]
+++
Let $A_0$ be an abelian variety over the finite field $k_0$ of [d-ab-field],
$A=A_0(\bar k)$, and $\ell\ne p$. Its rational Tate module has no nonzero
vector fixed by geometric Frobenius:

$$
(V_\ell A)^F=0.
$$

## Proof

In the finite-field setting of [d-ab-field], the fixed points of
$x\mapsto x^q$ in $\bar k$ are exactly $k_0$: the $q$ elements of $k_0$
exhaust the roots of $T^q-T$. On affine charts this gives
$A^\sigma=A_0(k_0)$, a finite group, since a point of a finitely generated
$k_0$-algebra is determined by finitely many values in $k_0$.
Apply [lem-tate-module-no-fixed] to the abelian group $A$ and the automorphism
$\sigma$; it gives $(V_\ell A)^\sigma=0$, and also $(V_\ell A)^F=0$ for
$F=\sigma^{-1}$.
