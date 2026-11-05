+++
id = "definition-tate-module--1"
kind = "definition"
title = "Tate module (1)"
name_showing = false
order = 1508001
aliases = ["bp-r470-1"]
lean = ["AlgebraicGeometry.IsAbelianVariety.tateModule"]
uses = ["definition-abelian-variety", "lemma-abelian-variety-commutative"]
+++
Let $A$ be an abelian variety over $k$ and let $\ell$ be a prime
invertible in $k$. The *Tate module* of $A$ is

$$
T_\ell A=\varprojlim_n A[\ell^n](\bar k),
$$

the limit taken along the maps $[\ell]:A[\ell^{n+1}](\bar k)\to
A[\ell^n](\bar k)$,
