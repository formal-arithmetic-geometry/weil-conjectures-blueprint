+++
kind  = "proof"
of    = "lem-pc-euler-characteristic-well-defined"
+++
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
