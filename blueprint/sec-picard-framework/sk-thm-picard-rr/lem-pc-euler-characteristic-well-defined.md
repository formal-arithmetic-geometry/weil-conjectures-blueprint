+++
id = "lem-pc-euler-characteristic-well-defined"
kind = "lemma"
title = "Well-definedness of the Euler characteristic"
order = 734
uses = ["def-pc-morphism-conventions", "lem-pc-coherent-hi", "lem-pc-curve-coherent-finiteness"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$ and $\mathcal{F}$ a coherent
$\mathcal{O}_X$-module. Then the set
$\{i:H^i(X,\mathcal{F})\neq0\}$ is finite and each $H^i(X,\mathcal{F})$ is a finite
dimensional $k$-vector space; hence
$\chi(X,\mathcal{F})=\sum_i(-1)^i\dim_kH^i(X,\mathcal{F})$ is well defined.

## Proof

Apply [lem-pc-coherent-hi] to the proper structure morphism
$f:X\to S=\operatorname{Spec}(k)$; the base $S$ is Noetherian and
quasi-compact. Since $S$ is affine, $H^i(X,\mathcal{F})=\Gamma(S,R^if_*\mathcal{F})$
is a finite $k$-module, that is, a finite-dimensional $k$-vector
space. Since $S$ is quasi-compact, $R^if_*\mathcal{F}=0$, hence
$H^i(X,\mathcal{F})=0$, for all $i\gg0$; and $H^i=0$ for $i<0$. So only
finitely many $H^i(X,\mathcal{F})$ are nonzero, and the alternating sum
of their dimensions is well defined. (For a smooth projective curve
over an algebraically closed field the same conclusion is also
[lem-pc-curve-coherent-finiteness].)
