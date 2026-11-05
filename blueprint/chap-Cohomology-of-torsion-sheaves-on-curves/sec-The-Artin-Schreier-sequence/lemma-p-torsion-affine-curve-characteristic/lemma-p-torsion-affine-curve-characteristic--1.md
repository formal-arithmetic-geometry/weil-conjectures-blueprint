+++
id = "lemma-p-torsion-affine-curve-characteristic--1"
kind = "lemma"
title = "$p$-torsion on an affine curve in characteristic $p$ (1)"
name_showing = false
order = 1587001
aliases = ["bp-r495-1"]
lean = []
uses = ["definition-classical-pro-etale-sheaves"]
+++
This quotient description is bypassed by the Lean route: the mainline
uses the higher-degree vanishing in
[lemma-p-torsion-affine-curve-characteristic--2] and has no separate
declaration identifying this $H^1$ with the quotient.

If $U$ is affine over an algebraically closed field $k$ of
characteristic $p$, then, for the classical constant sheaf $\mathbf F_p$ and
$\varphi(a)=a^p$ on $\Gamma(U,\mathcal O_U)$, we have

$$
H^1(U,\mathbf F_p)=
\Gamma(U,\mathcal O_U)/(\varphi-1)\Gamma(U,\mathcal O_U).
$$
