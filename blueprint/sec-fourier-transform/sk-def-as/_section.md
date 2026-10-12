+++
id = "sk-def-as"
kind = "definition"
title = "The Artin–Schreier sheaf"
order = 2980
lean = ["AlgebraicGeometry.Etale.artinSchreierSheaf"]
uses = ["sk-def-char"]
tags = ["sketch"]
+++
Let $k$ be a finite field with $q$ elements, $\Lambda$ a commutative ring
in which $q$ is invertible, and $\Psi:(k,+)\to\Lambda^\times$ an additive
character. The Artin–Schreier map $\mathrm{AS}_q:\Aone_k\to\Aone_k$,
$x\mapsto x^q-x$, satisfies $\mathrm{AS}_q\circ\sigma_a=\mathrm{AS}_q$
for the translations $\sigma_a:x\mapsto x+a$ ($a\in k$), which therefore
act on $(\mathrm{AS}_q)_*\Lambda$. The *Artin–Schreier sheaf*
$\mathcal L_\Psi$ on $\Aone_k$ is the $\Psi$-isotypic component

$$
\mathcal L_\Psi:=\operatorname{im}\bigl(e_\Psi\mid(\mathrm{AS}_q)_*\Lambda\bigr),\qquad
e_\Psi=\frac1q\sum_{a\in k}\Psi(-a)\,\sigma_a ,
$$

on which each $\sigma_a$ acts by $\Psi(a)$. For a $k$-scheme $X$ and
$f\in\Gamma(X,\mathcal O_X)$, viewed as $f:X\to\Aone_k$, put
$\mathcal L_{\Psi,f}:=f^*\mathcal L_\Psi$. For the character $\psi$ of
[sk-def-char] write $\mathcal L_{\psi,f}$, $\mathcal L_{\psi(af)}:=\mathcal L_{\psi,af}$
for $a\in k_0$, and on $\Aone$, $\mathcal L_\psi=\mathcal L_{\psi,x}$ and
$\mathcal L_{\psi(ax)}=\mathcal L_{\psi,ax}$.
