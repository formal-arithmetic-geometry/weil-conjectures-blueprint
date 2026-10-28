+++
id = "sk-prop-sp-tower-geometric"
kind = "proposition"
title = "The tower model of the smooth adjunction"
order = 3309
uses = ["sk-def-sp-normalized-towers", "sk-lem-sp-tower-levels", "sk-lem-sp-tower-bound", "sk-lem-sp-reduction", "sk-prop-geo-p1-adjunction", "sk-lem-sp-finite-existence", "sk-prop-an", "sk-thm-dnc"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. There is an
adjunction

$$
Rf_{!,\bullet}\dashv f_\bullet^!
\quad\text{between }\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)
\text{ and }\Dctf(Y_{\mathrm{proét}},\mathcal O_E/\ell^\bullet).
$$

On a coordinate chart $f|_U=p_d\circ e$ the right adjoint is
$e_\bullet^*p_{d,\bullet}^*(-)(d)[2d]$. At each level $n$ the unit and counit
are those of the finite adjunction; in particular
$(f_\bullet^!C_\bullet)_n\simeq f_{\mathcal O_E/\ell^n}^!C_n$ in
$\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^n)$, and the reduction maps of
$f_\bullet^!C_\bullet$ are induced by those of $C_\bullet$ and the coefficient
comparisons of [sk-lem-sp-reduction].
