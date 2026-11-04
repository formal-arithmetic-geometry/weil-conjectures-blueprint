+++
id = "example-compactness-finite-field--1"
kind = "example"
title = "Compactness over a finite field (1)"
name_showing = false
order = 432001
aliases = ["bp-r132-1"]
+++
Let $X=\operatorname{Spec}\mathbf F_q$ and $\Lambda=E$. Then
$\Ext^n(E,E)=H^n(X_{\mathrm{pro}\acute{e}t},E)$ is $E$ for $n=0,1$ and vanishes for
$n\geq2$. To see the vanishing, consider first $\mathbf Z_\ell$ and the Milnor sequence
(2.11) with $F_m=(\mathbf Z/\ell^m)_X$. Since
the field $\mathbf F_q$ has $\ell$-cohomological dimension one, we have
$H^n(X,\mathbf Z/\ell^m)=0$ for $n\ge2$ and all $m$. The finite
groups $H^1(X,\mathbf Z/\ell^m)$ have vanishing $\varprojlim^1$. The
Milnor sequence therefore gives $H^n(X_{\mathrm{pro}\acute{e}t},\mathbf Z_{\ell,X})=0$ for
$n\geq2$. Inverting $\ell$ and using
Example [example-first-cohomology-finite-field] for $n=1$ gives the
claim for $\mathbf Q_\ell$; for $E\neq\mathbf Q_\ell$ we tensor with $E$ over $\mathbf Q_\ell$.

As in the example over $\mathbf R$, products are exact
(Proposition [proposition-exact-products]) and the complexes $E[n]$
live in distinct degrees.
