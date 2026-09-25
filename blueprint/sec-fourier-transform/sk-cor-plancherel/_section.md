+++
id = "sk-cor-plancherel"
kind = "section"
title = "P9: Plancherel"
order = 2708
uses = ["sk-lem-orthogonality", "sk-thm-fourier-trace-formula"]
+++
*Corollary (sketch).*

For every $n\ge1$ and every Weil complex $K$ on $\Aone$,

$$
\sum_{y\in\mathbf F_{q^n}}\bigl|t_{\FT_\psi(K)}(y)\bigr|^2
=q^n\sum_{x\in\mathbf F_{q^n}}\bigl|t_K(x)\bigr|^2 .
$$

(Blueprint cor:fd-plancherel.)

## Proof

Insert the finite Fourier sum of P8, multiply by its conjugate and sum over
$y$:

$$
\sum_y\Bigl|\sum_xt_K(x)\psi_n(xy)\Bigr|^2
=\sum_y\sum_{x,x'}t_K(x)\overline{t_K(x')}\,\psi_n\bigl((x-x')y\bigr);
$$

the orthogonality of [sk-lem-orthogonality] makes the inner $y$-sum $q^n$
on the diagonal and $0$ off it, which is the identity. This is the classical
Plancherel theorem for the finite group $(\mathbf F_{q^n},+)$, transported to
trace functions; no weight enters.

Uses: [sk-lem-orthogonality], [sk-thm-fourier-trace-formula]
