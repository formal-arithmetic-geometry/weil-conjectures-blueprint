+++
id = "cor-fd-plancherel"
kind = "theorem"
title = "Plancherel identity"
order = 2952
tags = ["latex:corollary"]
uses = ["def-fd-trace-function", "def-fd-transform", "lem-fd-additive-orthogonality", "thm-fd-fourier-trace"]
+++
For every $n\ge1$,

$$
\sum_{y\in\mathbf F_{q^n}}
\left|t_{\operatorname{FT}_\psi(K)}(y)\right|^2
=q^n\sum_{x\in\mathbf F_{q^n}}
\left|t_K(x)\right|^2,
$$

for every Weil complex $K$ whose trace values are interpreted through a fixed $\iota:\Qlb\xrightarrow{\sim}\mathbf C$.

## Proof

Insert the finite Fourier sum of [thm-fd-fourier-trace], multiply it by its complex conjugate, and sum over $y$:

$$
\sum_{y}\Bigl|\sum_x t_K(x)\psi_n(xy)\Bigr|^2
=\sum_{y}\sum_{x,x'}t_K(x)\overline{t_K(x')}\ \psi_n((x-x')y).
$$

The orthogonality relation [lem-fd-additive-orthogonality] makes the inner $y$-sum equal to $q^n$ when $x=x'$ and zero otherwise. The surviving diagonal sum is exactly the right-hand side written with the absolute values of the trace function of [def-fd-trace-function].
