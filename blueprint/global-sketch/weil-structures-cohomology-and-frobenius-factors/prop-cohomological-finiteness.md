+++
id = "prop-cohomological-finiteness"
kind = "theorem"
title = "Compact-support finiteness and Frobenius"
order = 96
tags = ["latex:proposition"]
uses = ["def-cohomology-complexes", "def-derived-weil-object", "def-global-geometric-frobenius", "def-weil-compact-support-object", "def-weil-finite-coefficient-datum", "prop-compact-support-coefficient-passage", "prop-proper-operation-comparison"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{E,\Qlb\}$. Let $Y_0/\Fq$ be separated and of finite
type, let $Y$ be its geometric fiber, and let
$K\in D^b_c(Y,\Lambda)$ be equipped with
$\theta_K:Lg_Y^*K\xrightarrow{\sim}K$. For every $i\in\mathbf Z$,
$H_c^i(Y,K)$ is
finite-dimensional, vanishes outside a finite interval,
and carries a geometric Frobenius automorphism. If $Y_0$ is proper, then
for every $i\in\mathbf Z$ the
canonical isomorphism

$$
H_c^i(Y,K)\xrightarrow{\sim}H^i(Y,K)
$$

is Frobenius-equivariant.
If $Y$ has dimension $e$ and $K=\Lambda_Y[0]$ has its canonical derived
Weil object structure, then for every $i\in\mathbf Z$,

$$
H_c^i(Y,\Lambda)=0\qquad\text{for }i<0\text{ or }i>2e.
$$

For proper $Y$, the same range holds for ordinary cohomology. In
particular, if $Y$ is proper of pure dimension $e$, then
$H^i(Y,\Lambda)=0$ for $i\notin[0,2e]$.
