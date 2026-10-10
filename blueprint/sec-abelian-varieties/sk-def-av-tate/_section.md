+++
id = "sk-def-av-tate"
kind = "definition"
title = "$\\ell$-adic Tate module"
lean = ["AlgebraicGeometry.IsAbelianVariety.tateModule"]
order = 469
tags = ["sketch"]
+++
Let $A$ be an abelian variety over a field $k$, with algebraic closure
$\bar k$, and let $\ell$ be a prime. The *$\ell$-adic Tate module* of $A$ is the inverse
limit

$$
T_\ell A:=\varprojlim_n A[\ell^n](\bar k),
$$

the transition map from level $n+1$ to level $n$ being multiplication
by $\ell$; its rational form is $V_\ell A:=T_\ell A\otimes_{\Z_\ell}\Q_\ell$.
Every endomorphism of $A$, and every semilinear automorphism of
$A_{\bar k}$ over an automorphism of $k$, acts componentwise on
$T_\ell A$, so that $T_\ell A$ is a $\Z_\ell$-module with an action of
$\operatorname{Gal}(\bar k/k)$ in the arithmetic case.
