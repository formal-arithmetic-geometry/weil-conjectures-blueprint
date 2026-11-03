+++
id = "prose-04-21"
kind = "hidden"
title = "Finite and $\\ell$-adic coefficients"
order = 223
+++
For finite rings $A$ the coefficient sheaf $A_X$ is the usual constant
sheaf (Section [sec-n-coefficients]), so proper base change for torsion
complexes (Theorem [sk-thm-properbasechange]) applies directly. For $\mathcal O_E$, Theorem [sk-thm-properbasechange] gives proper base change at
each finite level $\mathcal O_E/\pi_E^n$, and the problem is to pass
to the limit.

By Theorem [sk-thm-pe-constructible-comparison], bounded constructible
complexes with finite coefficients on quasi-compact quasi-separated
schemes are classical. Hence the theorem, with $\Lambda=A$, applies to every
$K\in D^b_{\mathrm{ctf}}(X,A)$ for schemes of finite type over $k$.

The passage from finite coefficients to $\mathcal O_E$ is a question
of completeness. The inverse image
$g^*:D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)\to D(Y'_{\mathrm{pro}\acute{e}t},\mathcal O_E)$,
which is exact on sheaves of modules, need not preserve derived completeness. For
$M\in D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, we define its *completed inverse
image* $\hat g^*M\in D(Y'_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ by

$$
\hat g^*M
=R\varprojlim_n g^*(M\otimes^{\mathbf L}_{\mathcal O_{E,Y}}
(\mathcal O_E/\pi_E^n)_Y).
$$

For $Y$ and $Y'$ of finite type over $k$ and
$M\in D^b_{\mathrm{ctf}}(Y,\mathcal O_E)$, the criterion for integral
constructibility (Proposition [sk-prop-integral-criterion]) and the local
description of constructible sheaves in Definition [sk-def-sfb-constructible] show that $\hat g^*M=g^*M$. Until we know that proper direct
image preserves constructibility, we can only state base change with the
completed inverse image.
